##########################################
#
# p11650 [좌표 정렬하기]
#
# [문제]
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로,
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# [입력]
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# [출력]
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
#
# [https://www.acmicpc.net/problem/11650]
#
#
##########################################
# IMPORT
##########################################
from typing import List, Dict, Tuple
import sys
#
#
# FOR FAST INPUT
#
#
input = sys.stdin.readline
##########################################
# INPUT
##########################################
#
# 점의 개수, N
#
N = int(input())
#
# (int, int) 형태의 Tuple로 (x, y) 좌표를 입력 받아 List에 저장
#
coords = []
#
# N회 만큼 (x, y) 입력 받음
#
for _ in range(N):
    #
    #
    # 각 줄은 "0 4"와 같이 공백으로 구분된 문자열이 입력됨
    # split으로 "0", "4"로 쪼개준 다음
    # list(map(int, ["0", "4"])) 함수를 호출하면
    # int("0"), int("4")를 원소로 갖는 List 생성
    #
    #
    c = list(map(int, input().split()))
    #
    # 이를 다시 튜플로 만들어서 coords List에 저장
    #
    coords.append((c[0], c[1]))
##########################################
# SORT
##########################################
#
# sort 함수를 통해 coords List에 있는 요소를
# c[1](y)에 대한 오름차순으로,
# 만약 y가 같으면 x에 대한 오름차순으로 정렬
#
coords.sort(key=lambda c: (c[0], c[1]))
##########################################
# OUTPUT
##########################################
for c in coords:
    print(c[0], c[1])
