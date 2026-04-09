# 사용자 정보 입력 프로그램 (학년 포함)

# 사용자에게 정보를 입력 받음
name = input("이름을 입력하세요 : ")
student_id = input("학번을 입력하세요 : ")
major = input("학과를 입력하세요 : ")
grade = input("학년을 입력하세요 (숫자만) : ")

# 입력받은 정보를 출력
print("\n출력:")
print(f"이름: {name}")
print(f"학번: {student_id}")
print(f"학과: {major}")
print(f"학년: {grade}")