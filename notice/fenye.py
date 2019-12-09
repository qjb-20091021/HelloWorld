from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

def split_page(object_list, request, per_page=8):
    paginator = Paginator(object_list, per_page)
    # ȡ����ǰ��Ҫչʾ��ҳ��, Ĭ��Ϊ1
    page_num = request.GET.get('page', default='1')
    # ����ҳ��ӷ�ҳ����ȡ����Ӧҳ������
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger as e:
        # �����������ص�һҳ����
        page = paginator.page('1')
        page_num = 1
    except EmptyPage as e:
        # ������ҳ����ڻ�С��ҳ�뷶Χʱ,�ᴥ�����쳣
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # ���� ��ȡ���һҳ���ݷ���
            page = paginator.page(paginator.num_pages)
        else:
            # С�� ��ȡ��һҳ
            page = paginator.page(1)

    # �ⲿ����Ϊ�����д�������ʱ����Ȼ��֤����ʾ��ҳ������������10��
    page_num = int(page_num)   #��ǰҳ��
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif page_num >= 6 and page_num <= paginator.num_pages - 5:
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)
    print(dis_range)
    data = {'page': page, 'paginator': paginator, 'dis_range': dis_range }
    return data
