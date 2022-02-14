# variable
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m  = "CC#BCC#BCC#BCC#B"

# function
def solution(m, musicinfos):
    answer = ''
    ans_list = {}
    
    for music in musicinfos:
        music_seq = []
        
        tmp = music.split(',')
        
        # time
        h1 = int(tmp[0].split(':')[0])
        m1 = int(tmp[0].split(':')[1])
        h2 = int(tmp[1].split(':')[0])
        m2 = int(tmp[1].split(':')[1])
        if m2 < m1:
            h2 -= 1
            m2 += 60
        h = h2 - h1
        min = m2 - m1
        times = h*60 + min
        
        # make sequence
        m_s = ""
        tmp[3] = tmp[3].replace('C#', 'c')
        tmp[3] = tmp[3].replace('D#', 'd')
        tmp[3] = tmp[3].replace('F#', 'f')
        tmp[3] = tmp[3].replace('G#', 'g')
        tmp[3] = tmp[3].replace('A#', 'a')
        
        m = m.replace('C#', 'c')
        m = m.replace('D#', 'd')
        m = m.replace('F#', 'f')
        m = m.replace('G#', 'g')
        m = m.replace('A#', 'a')
        
        for i in range(times):
            s = tmp[3][i%len(tmp[3])]
            m_s += s
            
        if m in m_s:
            ans_list[tmp[2]] = times
            
            
    s_dict = sorted(ans_list.items(), key = lambda item : item[1], reverse = True)
    
    
    if len(ans_list) > 0:
        return s_dict[0][0]
    else: 
        return "(None)"
print(solution(m,musicinfos))