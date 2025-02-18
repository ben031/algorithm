def solution(numbers, hand):
    l,r = '*', '#' #초기값 설정
    anwser = '' 
    
    def dt(now, after) : #numbers in [2,5,8,0]일 때 거리구하는 함수
        pad = {1:(0,0), 2:(0,1), 3:(0,2),
              4:(1,0), 5:(1,1), 6:(1,2),
              7:(2,0), 8:(2,1), 9:(2,2),
              '*':(3,0), 0:(3,1), '#':(3,2)}

        now_x, now_y = pad[now]
        after_x, after_y = pad[after]

        return abs(after_x-now_x)+abs(after_y-now_y) #점과 점 사이 거리

    for i in numbers : #L
        if i in [1,4,7] :
            anwser+='L'
            l = i
        elif i in [3,6,9] : #R
            anwser+='R'
            r = i
        elif i in [2,5,8,0] : #M
            l_dt = dt(l, i)
            r_dt = dt(r, i)
            if l_dt < r_dt :
                anwser += 'L'
                l = i
            elif l_dt == r_dt :
                if hand == 'right' :
                    anwser+='R'
                    r = i
                else :
                    anwser+='L'
                    l = i
            else :
                anwser+='R'
                r = i
    return anwser

