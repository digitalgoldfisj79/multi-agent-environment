# Zenodo release checklist

For each paper:

1. Complete theorem-level cold review and citation verification.
2. Reserve a Zenodo DOI before freezing the PDF.
3. Insert the reserved DOI into the manuscript, CITATION.cff and metadata JSON.
4. Rebuild PDF, DOCX and LaTeX.
5. Re-run the repository validators listed in the supporting-materials manifest.
6. Verify the checksum manifest.
7. Upload the PDF and source files, or the prepared ZIP.
8. Set the PDF as the default Zenodo preview.
9. Preview the record and confirm author name and ORCID.
10. Publish a new version rather than silently replacing substantive files.

Zenodo currently supports up to 100 files and 50 GB per record and recommends ZIP packaging for deposits containing 20 or more files.
