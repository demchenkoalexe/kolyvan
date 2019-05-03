from django.db import models

class AuthorProduct(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)

	class Meta:
		db_table = "author_product"

class ListStone(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	description = models.TextField()

	class Meta:
		db_table = "list_stone"

class StoneProduct(models.Model): 
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	id_author = models.ForeignKey(AuthorProduct, on_delete=models.PROTECT)
	size_length = models.IntegerField()
	size_height = models.IntegerField()
	id_list_materials = models.ForeignKey(ListStone, on_delete=models.PROTECT)
	description = models.TextField()
	image = models.CharField(max_length=200)
	full_description = models.TextField()

	class Meta:
		db_table = "stone_product"