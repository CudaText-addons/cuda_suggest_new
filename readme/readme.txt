Plugin for CudaText.

1) On saving untitled document, CudaText suggests (in the "Save as" dialog) file name "new".
This plugin replaces that "new" with the first non-empty document line (from first 10 lines).
With replacing spaces with '_'.
So if the first non-empty line is " aa bb cc", plugin will make the filename "aa_bb_cc".
2) Plugin also changes 'UntitledN' ui-tab title to the title from text, on editing.

File extension (e.g. ".md") is added automatically by CudaText, from the active lexer.

Author: Alexey Torgashin (CudaText)
License: MIT