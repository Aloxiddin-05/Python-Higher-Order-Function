## 🔹 1-DARAJA (Asosiy tushunchalarni mustahkamlash)

### 1. Foydali sonlarni ajratish

Berilgan ro'yxatdan musbat sonlarni `filter()` yordamida ajrating.

```python
numbers = [4, -2, 0, 7, -9, 3, -1, 5]
```

### 2. Har bir sonni kvadratga oshiring

`map()` yordamida quyidagi ro'yxatdagi har bir sonni kvadratga oshiring.

```python
nums = [1, 2, 3, 4, 5]
```

### 3. Eng kichik va eng katta

`min()` va `max()` yordamida quyidagi ro'yxatdan eng kichik va eng katta sonni toping.

```python
numbers = [18, 29, 3, 45, 7, 12]
```

### 4. Alfavit tartibida saralash

`sorted()` yordamida ismlarni alfavit tartibida saralang.

```python
names = ["Zafar", "Ali", "Sami", "Bekzod"]
```

### 5. `lambda` bilan ko'paytirish

Har bir elementni 5 ga ko'paytirish uchun `map()` va `lambda`dan foydalaning.

```python
nums = [2, 4, 6, 8]
```

---

## 🔹 2-DARAJA (Oraliq daraja, real hayotga yaqinlashtirish)

### 6. Email domenlarini ajratish

Quyidagi email ro’yxatidan faqat `gmail.com` domeniga tegishlilarni ajrating.

```python
emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
```

### 7. Narxlarni \$ belgisiz olish

Quyidagi narxlar ro’yxatidan `$` belgisiz faqat raqamlarni ajrating (lambda bilan).

```python
prices = ["$120", "$340", "$50", "$90"]
```

### 8. Yoshi bo'yicha sortlash

Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.

```python
people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
```

### 9. Eng uzoq ismni toping

`max()` va `lambda` yordamida eng uzun ismni toping:

```python
names = ["Ali", "Valijon", "Sami", "Diyorbek"]
```

---

## 🔹 3-DARAJA (Chuqur tushunish, funksional yondashuv)

### 10. Matndan raqamlarni ajratish

Berilgan matndan faqat sonlarni ajrating:

```python
text = ["apple", "34", "banana", "100", "abc", "75"]
```

> Natija: `['34', '100', '75']`

### 11. Juft sonlarning kvadratlari

Faqat juft sonlarni tanlab, ularning kvadratlarini `filter()` + `map()` bilan hisoblang.

```python
nums = list(range(1, 21))
```

### 12. Talabalarni baho bo‘yicha tartiblang

Baholar bo‘yicha saralash (kichikdan katta):

```python
students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]
```

### 13. Top 3 eng uzun so‘z

Matndagi eng uzun 3 ta so‘zni toping:

```python
sentence = "Functional programming in Python is very powerful and elegant"
```

> Foydalaning: `sorted()`, `lambda`, `split()`, `[:3]`

### 14. list.sort bilan joyida o'zgartirish

Quyidagi ro’yxatni uzunlik bo‘yicha joyida sort qiling:

```python
words = ["sun", "mountain", "a", "apple"]
```

> `list.sort(key=lambda ...)` ishlatilishi kerak.

---

## 🔹 4-DARAJA (Chuqur tahlil va kompozitsiya)

### 15. Tanlovlar ro'yxatidan eng ko'p ovoz olganini topish

Har bir tanlovda necha ovoz borligini bilgan holda eng ko'p ovoz olgan variantni aniqlang.

```python
votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
```

> `max(..., key=lambda x: x["votes"])`

### 16. `lambda` bilan ro'yxatni qisqartirish

Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:

```python
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
```