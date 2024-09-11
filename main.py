import torch
from train import Train

def main():
    
    path = "./dataset/10times"
    
    train = Train(dataset_path = path)
    train.make_dataset(trial = 1)
    train.execute()
    pass

if __name__ == "__main__":
    main()