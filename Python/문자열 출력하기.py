문제 설명
문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 1,000,000
str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.

문제 풀이
str = input()
if len(str)>=1 and len(str)<=1000000 and str!='':
    print(str)
