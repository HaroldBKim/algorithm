from collections import defaultdict


def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for c_name, c_type in clothes:
        clothes_dict[c_type] += 1
    for i in clothes_dict.values():
        answer *= (i + 1)
    return answer - 1


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
