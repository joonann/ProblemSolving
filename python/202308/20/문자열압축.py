# 문자열 압축
# 반복되는 문자열 활용해 문자열 압축

def solution(s):
	answer = 1001
	if len(s) <= 2:
		return len(s)
	# 완전 탐색을 이용해 절반 길이로 압축한 경우까지 고려한다.
	for i in range(1, len(s) // 2 + 1):
		l = 0 # 압축할 문자열의 길이가 i인 경우 압축 문자열 길이
		str_l = []
		tmp_s = s
		while tmp_s:
			# tmp_s에서 앞에 i 개만큼 자른다
			now = tmp_s[:i]
			tmp_s = tmp_s[i:]
			# 아직 자른 문자열이 없는 경우(맨처음 문자열)
			if not str_l:
				str_l.append([now, 1])
			# 두번째부터는 -1의 인덱스로 같은지 검사하고 다르면 append
			else:
				if now == str_l[-1][0]:
					str_l[-1][1] += 1
				else:
					str_l.append([now, 1])
			
		# str_l에 들어가 있는 문자열들을 돌면서 str(개수)와 문자열의 길이 더해줌
		for a in str_l:
			if a[1] <= 1:
				l += len(a[0])
			else:
				l += len(a[0]) + len(str(a[1]))
		answer = min(answer, l)

	return answer
