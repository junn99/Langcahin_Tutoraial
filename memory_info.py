import psutil

# 시스템의 메모리 정보 가져오기
memory_info = psutil.virtual_memory()

# 총 메모리와 사용 가능한 메모리 출력
total_memory_gb = memory_info.total / (1024 ** 3)  # GB로 변환
available_memory_gb = memory_info.available / (1024 ** 3)  # GB로 변환

print(f"총 시스템 메모리: {total_memory_gb:.2f} GB")
print(f"사용 가능한 메모리: {available_memory_gb:.2f} GB")
