from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别')
    is_nav = models.BooleanField(default=True, verbose_name='是否展示')
    sequence = models.PositiveIntegerField(default='255', verbose_name='显示顺序')

    def __str__(self):
        return self.name 

    class Meta:
    	verbose_name = verbose_name_plural = '类别'


class Author(models.Model):

	SEX_MALE = 0 
	SEX_FEMALE = 1
	SEX_UNKNOWN = 2 
	SEX_ITEMS = (
		(SEX_MALE, '男'),
		(SEX_FEMALE, '女'),
		(SEX_UNKNOWN, '未知')
	)
	name = models.CharField(max_length=50, verbose_name='姓名')
	sex = models.PositiveIntegerField(default=SEX_UNKNOWN, choices=SEX_ITEMS, verbose_name='性别')
	country = models.CharField(max_length=50, verbose_name='国家', blank=True, null=True)
	bron_date = models.DateField(verbose_name='出生日期', null=True, blank=True)
	dead_date = models.DateField(verbose_name='逝世日期', null=True, blank=True)
	title = models.CharField(max_length=50, verbose_name='头衔', blank=True, null=True)
	url = models.URLField(verbose_name='链接', null=True, blank=True)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = verbose_name_plural = '作者'


class Books(models.Model):
    """书籍类"""

    name = models.CharField(max_length=50, verbose_name='书名')
    author = models.ForeignKey(Author, verbose_name='作者', on_delete=models.SET_NULL, null=True)
    translator = models.CharField(max_length=50, verbose_name='译者', blank=True, null=True)
    publisher = models.CharField(max_length=50, verbose_name='出版社')
    published_date = models.DateField(verbose_name='出版时间')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='img',max_length=100, verbose_name='图片', null=True, blank=True)
    interduction = models.TextField(max_length='512', verbose_name='简介')
    
    def __str__(self):
    	return self.name

    class Meta:
    	verbose_name = verbose_name_plural = "书籍"

	
