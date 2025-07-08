from pdfminer.high_level import extract_text

pdf_path = r"C:\Users\NIPS-2017-attention-is-all-you-need-Paper.pdf"

# PDF → 텍스트 추출
text = extract_text(pdf_path)

# 결과를 txt 파일로 저장
output_path = r"C:\Users\output.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("PDF 텍스트 추출 완료!")
