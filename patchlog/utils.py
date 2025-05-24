import zipfile
import os
import shutil

BASE_PATCH_DIR = 'base_patches'
OUTPUT_ZIP_PATH = 'output/merged_patch.zip'

def extract_zip_to_folder(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("✅ zip 압축 해제 완료:", zip_path)

import zipfile
import os
import shutil

BASE_PATCH_DIR = 'base_patches'

def extract_zip_to_folder(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("압축 해제 완료:", zip_path)

def merge_and_zip(new_patch_zip_path, output_zip_path):
    print("병합 함수 실행:", new_patch_zip_path)

    temp_dir = 'temp_patch'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    extract_zip_to_folder(new_patch_zip_path, temp_dir)

    # base_patches에 덮어쓰기
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), temp_dir)
            dest_path = os.path.join(BASE_PATCH_DIR, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(os.path.join(root, file), dest_path)

    print("base_patches 폴더 내 파일:")
    for root, dirs, files in os.walk(BASE_PATCH_DIR):
        for f in files:
            print("-", os.path.join(root, f))

    # 병합된 zip 파일 생성
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_count = 0
        for root, dirs, files in os.walk(BASE_PATCH_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, BASE_PATCH_DIR)
                zipf.write(abs_path, rel_path)
                file_count += 1
        print("병합 대상 파일 수:", file_count)
        print("병합 zip 생성 완료:", output_zip_path)
