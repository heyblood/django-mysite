import os
import sys

import django

import faker
from random import randint

# 将项目根目录添加到 Python 的模块搜索路径中
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def genaerate_data():

    # 消除多余的属性访问，提升运行效率
    article_create = ArticlePost.objects.create
    comment_create = Comment.objects.create

    print('Some articles and comments will be created, which may take a little time.')
    locales = ['', 'zh_CN']
    luanguages = ['English', 'Chinese']
    for locale, language in zip(locales, luanguages):
        print("Create articles and comments in {}...".format(language))
        fake = faker.Faker(locale=locale)  # 创建 Fake对象，设置语言
        # 消除属性访问
        fake_date_time_between = fake.date_time_between
        fake_paragraphs = fake.paragraphs
        fake_sentence = fake.sentence
        del fake

        i = None
        for i in range(1, 101):
            # 返回 2 个指定日期间的随机日期。三个参数分别是起始日期，终止日期和时区。
            created_time = fake_date_time_between(
                start_date='-1y',  # 1 年前
                end_date="now",  # 终止日期为当下
                tzinfo=get_current_timezone())
            post = article_create(
                title=fake_sentence().rstrip('.'),
                # 用 2 个换行符连起来是为了符合 Markdown 语法，Markdown 中只有 2 个换行符分隔的文本才会被解析为段落
                body='\n\n'.join(fake_paragraphs(randint(1, 20))),  # 10 个段落文本
                created=created_time,
                author=user,
                total_views=randint(10, i + 10),
            )
            post.save()
            # 为当前文件添加一些评论
            j = None
            for j in range(1, 6):
                comment = comment_create(article=post,
                                         user=user,
                                         body='\n\n'.join(fake_paragraphs(j)),
                                         created=created_time)
                comment.save()


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()

    # 加载 django 配置项
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.development")
    django.setup()  # 启动 django

    from django.utils.timezone import get_current_timezone
    from django.contrib.auth.models import User

    from article.models import ArticlePost
    from comment.models import Comment

    print('clear database.')
    ArticlePost.objects.all().delete()
    User.objects.all().delete()

    print('create a superuser.')
    user = User.objects.create_superuser('admin', '', 'admin')

    # 生成虚拟文章和评论
    genaerate_data()

    print('done!')
    print("It ran for {} seconds.".format(perf_counter() - start))
