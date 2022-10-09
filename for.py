#from tqdm import tqdm

#for _ in tqdm(range(10 ** 9)):
#  pass

sales_2020 = [4000, 5000, 6000]
sales_2021 = [5000, 3000, 2000]

for c, p in zip(sales_2021, sales_2020):
  result = (c / p - 1) * 100
  print(f'{result:.1f}%')
  
names = ['鈴木', '斎藤', '田中']

for i, n in enumerate(names):
  print(f'{i}位: {n}')
  

