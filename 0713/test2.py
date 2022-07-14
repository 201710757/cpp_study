import re
# from bs4 import BeautifulSoup
#url = re.search(r'(<meta property.+content=")(https://.*)"/>', p).group(2) #현재 url검색
# ex_url = re.findall(r'<a href="https://\S*">', p) #외부 링크 url 전부 검색
import re
# from bs4 import BeautifulSoup



# url = re.search(r'(<meta property.+content=")(https://.*)"/>', p).group(2) #현재 url검색
# ex_url = re.findall(r'<a href="https://\S*">', p) #외부 링크 url 전부 검색
def solution(word, pages):
    answer = 0
    a_tag = re.compile('href=.+">', re.DOTALL)
    # a_tag = re.compile('^<a href=.+</a>$', re.DOTALL)
    meta_tag = re.compile('<meta property="og:url" content=.+"/>', re.DOTALL)
    body_tag = re.compile('<body>.+</body>', re.DOTALL)
    score = [[0]*3]*len(pages)
    # return score
    
    real_meta = []

    info = {}
    for idx, page in enumerate(pages):
        cleanr = re.compile('\\n')
        page = re.sub(cleanr, ' ', page)
        # print(info)
        base_score = 0
        url = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2)
        print("URL : ", url)
        # url = url.split("\"")[3]
        real_meta.append(url)
        a_list = []
        ln = re.findall(r'<a href="https://\S*">', page)
        # print("ln : ", ln)
        for l in ln:
            a_list.append(l)

        link_num = len(a_list)#len(ln)
        # print("link n : ", link_num)
        # print(ln)
        # print(url.split("\"")[3])
        matching_score = 0
        
        _body = body_tag.findall(page)[0]
        _body = _body.lower()
        # print(_body.split(' '))
        _body = _body.replace('\t',' ')
        body = _body.split(' ')
        # body = body.split('\t')
        # print(body)
        out_link = {}
        
        for b in ln:
            # print("B : ", b)
            _tmp = b
            print(_tmp)
            if len(_tmp) > 0:
                # print("tag : ", _tmp[0].split("\"")[1])
                out_l = _tmp.split("\"")[1]
                # print("URL : ", url, " / out l : ", out_l)
                try:
                    out_link[out_l] += 1
                except:
                    out_link[out_l] = 1
        # _b = re.split(r'[ ,:]', b)
        for b in body:
            _b = " ".join(re.findall("[a-zA-Z]+", b))
            # print("_b : ", _b)
            # print("URL : ", url, " B : ", _b)

            # if b[:len(word)] == word.lower():
            # if word.lower() in _b:
            # # if b == word.lower():
            #     base_score += 1
            for bb in _b.split(' '):
                if word.lower() == bb:
                    base_score += 1

                # print("word  : ", b[:len(b)])
        
        # add link score 
        for (k, v) in out_link.items():
            try:
                info[k][2] += base_score/link_num
            except:
                info[k] = [0, 0, base_score/link_num]

        # base score, link num, matching score        
        try:
            info[url][0] += base_score
            info[url][1] += link_num
        except:
            info[url] = [base_score, link_num, 0]

        # print(a_tag.findall(page)[0].split('\"')[1])
        # for a in a_list:#a3_tag.findall(page):
        #     try:
        #         info[a][2] += base_score / link_num
        #     except:
        #         info[a] = [0, 0, 0]
        #         info[a][2] = base_score / link_num
    _info = {}
    for k, v in info.items():
        if k in real_meta:
            _info[k] = v
    # print(list(_info.items()))
    res = []
    for m in real_meta:
        res.append(_info[m])
    # print("RES : ", res)
    # res = [l_info[1][2]+l_info[1][0] for l_info in list(_info.items())]
# min(range(len(output)), key=f)
    # print(res)
    return max(range(len(res)), key=lambda i : (res[i][0] + res[i][2]))
    # return max(range(len(res)), key=lambda i : res[i])
    


def solution1(word, pages):
    answer = 0
    a_tag = re.compile('href=.+">', re.DOTALL) # re.compile('<a href="https:.\S"', re.DOTALL)#
    # a_tag = re.compile('^<a href=.+</a>$', re.DOTALL)
    meta_tag = re.compile('<meta property="og:url" content=.+"/>', re.DOTALL)
    body_tag = re.compile('<body>.+</body>', re.DOTALL)
    score = [[0]*3]*len(pages)
    # return score
    
    real_meta = []

    info = {}
    for idx, page in enumerate(pages):
        try:
            cleanr = re.compile('\\n')
            page = re.sub(cleanr, ' ', page)
            # print(info)
            base_score = 0
            try:
                url = meta_tag.findall(page)[0]
                url = url.split("\"")[3]
                real_meta.append(url)
            except:
                continue
            
            # print("URL : ", url)
            a_list = []
            try:
                ln = a_tag.findall(page)[0].split()
                for l in ln:
                    ll = a_tag.findall(l)[0]
                    # print("LL : " , ll.split("\""))
                    a_list.append(ll[1])
            except:
                continue

            link_num = len(a_list)#len(ln)
            # print("link n : ", link_num)
            # print(ln)
            # print(url.split("\"")[3])
            matching_score = 0
            try:
                _body = body_tag.findall(page)[0]
                _body = _body.lower()
                # print(_body.split(' '))
                _body = _body.replace('\t',' ')
                body = _body.split(' ')
            except:
                continue
            
            # body = body.split('\t')
            # print(body)
            out_link = {}
            try:
                for b in body:
                    # print("B : ", b)
                    _tmp = a_tag.findall(b)
                    if len(_tmp) > 0:
                        # print("tag : ", _tmp[0].split("\"")[1])
                        out_l = _tmp[0].split("\"")[1]
                        # print("URL : ", url, " / out l : ", out_l)
                        try:
                            out_link[out_l] += 1
                        except:
                            out_link[out_l] = 1
                    # _b = re.split(r'[ ,:]', b)
                    _b = " ".join(re.findall("[a-zA-Z]+", b))
                    # print("_b : ", _b)
                    # print("URL : ", url, " B : ", _b)

                    # if b[:len(word)] == word.lower():
                    # if word.lower() in _b:
                    # # if b == word.lower():
                    #     base_score += 1
                    for bb in _b.split(' '):
                        if word.lower() == bb:
                            base_score += 1

                        # print("word  : ", b[:len(b)])
            except:
                continue
            # add link score 
            for k, v in out_link.items():
                try:
                    info[k][2] += base_score/link_num
                except:
                    info[k] = [0.0, 0.0, base_score/link_num]

            # base score, link num, matching score        
            try:
                info[url][0] += base_score
                info[url][1] += link_num
            except:
                info[url] = [base_score, link_num, 0.0]

            # print(a_tag.findall(page)[0].split('\"')[1])
            # for a in a_list:#a3_tag.findall(page):
            #     try:
            #         info[a][2] += base_score / link_num
            #     except:
            #         info[a] = [0, 0, 0]
            #         info[a][2] = base_score / link_num
        except:
            continue
    _info = {}
    res = []

    try:
        for k, v in info.items():
            if k in real_meta:
                _info[k] = v
        for m in real_meta:
            res.append(_info[m])
    except:
        pass
    # print("RES : ", res)
    # res = [l_info[1][2]+l_info[1][0] for l_info in list(_info.items())]
    # min(range(len(output)), key=f)
    try:
        r = max(range(len(res)), key=lambda i : (res[i][0] + res[i][2]))
    except:
        r = 0
    
    return r
    # return max(range(len(res)), key=lambda i : res[i])

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
word = "Muzi"

print(solution(word, pages))