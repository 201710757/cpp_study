import re
# from bs4 import BeautifulSoup

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
        url = meta_tag.findall(page)[0]
        url = url.split("\"")[3]
        real_meta.append(url)
        # print("URL : ", url)
        a_list = []
        ln = a_tag.findall(page)[0].split()
        # print("ln : ", ln)
        for l in ln:
            try:
                ll = a_tag.findall(l)[0]
                # print("LL : " , ll.split("\""))
                a_list.append(ll[1])
            except:
                pass

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
            print("URL : ", url, " B : ", _b)

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
    print(list(_info.items()))
    res = []
    for m in real_meta:
        res.append(_info[m])
    # print("RES : ", res)
    # res = [l_info[1][2]+l_info[1][0] for l_info in list(_info.items())]
# min(range(len(output)), key=f)
    print(res)
    return max(range(len(res)), key=lambda i : (res[i][0] + res[i][2]))
    # return max(range(len(res)), key=lambda i : res[i])
    

# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

# word = "blind"
word = "Muzi"
print(solution(word, pages))


