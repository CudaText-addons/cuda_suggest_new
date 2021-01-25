import os
from cudatext import *

MAX_LINES = 10

class Command:
    
    def on_save_naming(self, ed_self):
        
        suggest = ''
        cnt = ed_self.get_line_count()
        for i in range(min(MAX_LINES, cnt)):
            line = ed_self.get_text_line(i).strip()
            print('line', line)
            if line:
                suggest = line.replace(' ', '_').replace('\t', '_')
                return suggest
