
'''
https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

'''

def solution(record):
    answer = []
    chat_msg = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    nic_dict = {}

    for r in record : 
        split = r.split()
        if len(split) > 2 : 
            nic_dict[split[1]] = split[2]

    for r in record :
        split = r.split()
        if split[0] != "Change" :
            answer.append(str(nic_dict[split[1]])+str(chat_msg[split[0]]))
    
    print("answer -> " + str(answer))
    
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print("답 : ", solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]