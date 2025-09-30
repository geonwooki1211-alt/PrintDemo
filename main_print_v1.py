# 1. 변수 선언
name = "squallki"
age = 25
score = 95.5

# 2. 기본 출력
print("Hello, Python!")

# 3. f-string (가장 많이 씀, Python 3.6+)
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format() 함수
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("My name is {}, age {}, score {}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))

# 5. printf형식 (C 스타일, 이전 방식)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 6. 여러 줄 출력 (줄바꿈 포함)
print("This is line 1\nThis is line 2")

# 7. end 옵션 (기본값은 줄바꿈 \n)
print("Hello", end=" ")
print("World!")

# 8. sep 옵션 (기본값은 공백)
print("2025", "09", "23", sep="-")

# 9. 딕셔너리/리스트 같은 출력
data = {"name": name, "age": age, "score": score}
print("Data:", data)

# 10. f-string과 예제산식/함수 사용
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

# 11. 딕셔너리와 f-string (''' 묶은 형태)
print(f'''
Student Info:
   - Name : {name}
   - Age  : {age}
   - Score: {score:.2f}
''')
