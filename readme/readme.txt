Plugin for CudaText.
On saving untitled document, CudaText suggests (in the "Save as" dialog) file name "new".
This plugin replaces that "new" with the first non-empty document line (counting only
first 10 lines). With replacing spaces with '_'.
So if the first non-empty line is " aa bb cc", plugin will make the filename "aa_bb_cc".

File extension (e.g. ".md") is added automatically by CudaText, from the active lexer.

Author: Alexey (CudaText)
License: MIT
