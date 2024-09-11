import csv
import torch
import random
from model import Model
from torch import Tensor


class Train():
    def __init__(self, dataset_path, orders = 10):
        self.dataset_path = dataset_path
        self.orders = orders
        self.model = Model(orders=self.orders)
        
        with open(f"{self.dataset_path}/train.csv") as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
            self.header = lines[0]
            self.datalist = [[int(item) for item in row] for row in lines[1:]]
    
    def make_dataset(self, trial):
        if trial <= 0 or len(self.datalist) < trial:
            raise Exception("ERROR: invalid trial number")
        self.trial = trial
        self.answer = self.datalist[self.trial - 1][:-1]
        self.bonus = self.datalist[self.trial - 1][-1]
        self.input = torch.rand(self.orders, 43)
    
    def execute(self):
        epoch = 1
        x = self.input
        for _ in range(epoch):
            x = self.model(x)
            self.calculate_loss(x)
        return
    
    def calculate_loss(self, pred_matrix: Tensor):
        with torch.no_grad():
            
            # 正解を生成
            # 3等以上と一致: そのまま
            # 4等以下, はずれ: 最も少ない値の変動で, 3等になれる組み合わせ
            pred_list = pred_matrix.tolist()
            for lottery in pred_list:
                sorted_lot = sorted(list(enumerate(lottery, start=1)), key=lambda x: x[1], reverse=True)
                print(sorted_lot)
    
    # 正解のテンソルを作成
    def make_answer_matrix(self, pred_list: list):
        
        for lottery in pred_list:
            hit_count = 0
            for value in lottery:
                pass
                
        print(pred_list)
        print(self.answer, self.bonus)
        pass