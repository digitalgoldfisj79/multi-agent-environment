#!/usr/bin/env python3
# Generate the exact TFP3 JSONL classifier from the frozen direct census source.
from __future__ import annotations
import argparse, hashlib
from pathlib import Path

EXPECTED_GIT_BLOB = "ae127e40f901039d3ac16600f025c0fb53333035"
SOURCE = Path(__file__).with_name("ff_large_field_cubic_falsification.cpp")

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def build(source: str) -> str:
    source = source.replace("#include <map>", "#include <map>\n#include <string>")
    source = source.replace(
        "struct Census { int p_orbits; int seed_orbits; long long incidences; };",
        '''struct Census { int p_orbits; int seed_orbits; long long incidences; };
void print_poly_json(const Poly& p) {
    std::cout << "[" << p.a[2] << "," << p.a[1] << "," << p.a[0] << "]";
}''')
    anchor = '''    return {static_cast<int>(representatives.size()), static_cast<int>(seeds.size()),
            static_cast<long long>(incidence_quads.size())};'''
    replacement = r'''    const int inv3 = inverse_scalar(3);
    for (const Seed& seed : seeds) {
        const int shift = modq(-1LL * band[seed.p].a[2] * inv3);
        const int lambda = seed.lambda;
        const Poly A = affine_transform(band[seed.p], lambda, shift);
        const Poly B = affine_transform(band[seed.s], lambda, shift);
        const Poly C = affine_transform(band[seed.pp], lambda, shift);
        const Poly D = affine_transform(band[seed.sp], lambda, shift);
        const int normalized_rho = modq(1LL * seed.rho * inverse_scalar(lambda));
        std::cout << "{\"type\":\"orbit\",\"q\":" << q
                  << ",\"rho\":" << normalized_rho << ",\"A\":";
        print_poly_json(A); std::cout << ",\"B\":"; print_poly_json(B);
        std::cout << ",\"C\":"; print_poly_json(C);
        std::cout << ",\"D\":"; print_poly_json(D); std::cout << "}\n";
    }
    return {static_cast<int>(representatives.size()), static_cast<int>(seeds.size()),
            static_cast<long long>(incidence_quads.size())};'''
    if anchor not in source:
        raise SystemExit("classifier return anchor not found")
    source = source.replace(anchor, replacement, 1)
    start = source.index("int main() {")
    main = r'''int main(int argc, char** argv) {
    const std::map<int,std::pair<int,long long>> frozen = {
        {5,{0,0}}, {7,{0,0}}, {11,{2,220}}, {13,{0,0}}, {17,{2,544}},
        {19,{2,684}}, {23,{0,0}}, {29,{2,1624}}, {31,{2,1860}},
        {37,{4,5328}}, {41,{6,9840}}, {43,{6,10836}}, {47,{2,4324}},
        {53,{6,16536}}, {59,{4,13688}}
    };
    std::vector<int> fields;
    bool regression = false;
    for (int i=1; i<argc; ++i) {
        const std::string argument = argv[i];
        if (argument == "--regression") regression = true;
        else fields.push_back(std::stoi(argument));
    }
    if (fields.empty())
        for (const auto& [field, ignored] : frozen) fields.push_back(field);
    bool ok = true;
    for (const int field : fields) {
        const Census got = run_census(field);
        std::cout << "{\"type\":\"summary\",\"q\":" << field
                  << ",\"P_orbits\":" << got.p_orbits
                  << ",\"true_orbits\":" << got.seed_orbits
                  << ",\"incidences\":" << got.incidences << "}\n";
        if (regression) {
            const auto it = frozen.find(field);
            if (it == frozen.end() || it->second.first != got.seed_orbits ||
                it->second.second != got.incidences) ok = false;
        }
    }
    return regression && !ok ? 1 : 0;
}
'''
    return source[:start] + main

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data = SOURCE.read_bytes()
    actual = git_blob_sha(data)
    if actual != EXPECTED_GIT_BLOB:
        raise SystemExit(f"frozen source blob mismatch: {actual}")
    args.output.write_text(build(data.decode()), encoding="utf-8")
    print(f"wrote {args.output}")

if __name__ == "__main__":
    main()
