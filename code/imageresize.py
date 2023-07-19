from PIL import Image
import os

# 원하는 크기 선택
size = (256, 256)

# 내 폴더에 있는 이미지 파일(png)들에 대해 작업 수행
for filename in os.listdir(r'C:\Users\USER\python_sunsh\betta\betta_refine\betta_fish_images_220\converted_png'):
    if filename.endswith('.png'):
        # Pillow 사용해서 이미지 열기
        with Image.open(os.path.join(r'C:\Users\USER\python_sunsh\betta\betta_refine\betta_fish_images_220\converted_png', filename)) as im:
            # 이미지 파일의 현재 크기
            current_width, current_height = im.size
           
            # 이미지 원하는 크기로 resize
            scale = min(size[0]/current_width, size[1]/current_height)
            new_width = int(current_width * scale)
            new_height = int(current_height * scale)
           
            # 기존의 해상도는 유지하도록
            im_resized = im.resize((new_width, new_height), Image.ANTIALIAS)
           
            # 새로운 이미지 생성
            new_im = Image.new('RGB', size, (0, 0, 0))
           
            # 마무리
            x_offset = int((size[0] - new_width)/2)
            y_offset = int((size[1] - new_height)/2)
            new_im.paste(im_resized, (x_offset, y_offset))
           
            # 원래 파일명 그대로 저장
            new_filename = os.path.join(r'C:\Users\USER\python_sunsh\betta\betta_refine\betta_fish_images_220\converted_png', filename)
            new_im.save(new_filename)