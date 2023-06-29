import requests as rq ,os as oo,json as jj
def data_upload():
    da={
        'q':'fish',
        "apikey":oo.environ['ne_key'],
        "language":"en",
        # 'country':'in',# country parameter is not supported...
    }
    try:
        with rq.get(url=r'https://newsapi.org/v2/everything', params=da) as mk:
            with open(r'../data/data_country.json','w+') as cv:
                jj.dump(fp=cv,
                        obj=mk.json(),
                        indent=5,

                )
            # print(type(mk.json()))

    except Exception as ep:
        print(ep)
    # for a in mk.json()["articles"]:
    #     print(a["urlToImage"])
        # if rq.head(url=a["urlToImage"]).status_code != 200:
        #     print(a["urlToImage"])

# data_upload()


def chek_dead_link():
    try:
        with open(r'../data/data.json','r',encoding='utf-8') as data:
            for a in jj.load(data)["articles"]:
                img=a['urlToImage']
                if img != None:
                    print(f"cheacking link ----{img}")
                    ap=rq.head(img).status_code
                    print(ap)
                    if ap != 200:
                        print(f'{ap}----dead link:{img}')
                    elif ap == 200:
                        print('good link')
                    # else:
                    #     print(ap)
                else:
                    print(img)

    except Exception as ep:
        print(ep)
        

# chek_dead_link()

da={
    a:chr(a)
    for a in range(65,65+26)
}
da.pop(65,'qo')
print(da)