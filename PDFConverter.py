import os
from fpdf import FPDF

class PDF(FPDF):
		current_x = 10
		current_y = 30
		block_num = 0
		
		def __init__(self, name):
				super().__init__()
				self.name = name
				current_dir = os.path.dirname(os.path.abspath(__file__))
				
				# font의 경로 정해주기
				regular_font_path = os.path.join(
						current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Regular.ttf"
				)
				bold_font_path = os.path.join(
						current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Bold.ttf"
				)
				italic_font_path = os.path.join(
						current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Ilalic.ttf"
				)
				korean_font_path = os.path.join(
						current_dir, "S_Core_Dream", "SCDream2.ttf"
				) # SCDream2
				korean_bold_font_path = os.path.join(
						current_dir, "S_Core_Dream", "SCDream5.ttf"
				) # SCDream5
				
				# font 추가하기
				self.add_font("JetBrainsMono", "", regular_font_path, uni=True)
				self.add_font("JetBrainsMono", "B", regular_font_path, uni=True)
				self.add_font("JetBrainsMono", "I", regular_font_path, uni=True)
				self.add_font("SCDream2", "", regular_font_path, uni=True)
				self.add_font("SCDream5", "B", regular_font_path, uni=True)
				
				# "": regular, "B": bold, "I": Italic
				
		# 이 뒷부분부터는 여러분들에게 코드를 제공하겠습니다.
		
				