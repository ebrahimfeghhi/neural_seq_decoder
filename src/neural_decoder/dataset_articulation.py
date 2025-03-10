import torch
from torch.utils.data import Dataset


class SpeechDataset(Dataset):
    
    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform
        self.n_days = len(data)
        self.n_trials = sum([len(d["sentenceDat"]) for d in data])
        self.neural_feats = []
        self.phone_seqs = []
        
        self.voiced_seqs = []
        self.place_seqs = []
        self.manner_seqs = []
        self.height_seqs = []
        self.backness_seqs = []
        self.roundedness_seqs = []
        
        self.neural_time_bins = []
        self.phone_seq_lens = []
        
        self.articulatory_seqs_lens = []

        self.days = []
        
        for day in range(self.n_days):
            for trial in range(len(data[day]["sentenceDat"])):
                self.neural_feats.append(data[day]["sentenceDat"][trial])
                self.phone_seqs.append(data[day]["phonemes"][trial])
                
                self.voiced_seqs.append(data[day]["voiced"][trial])
                self.place_seqs.append(data[day]["place"][trial])
                self.manner_seqs.append(data[day]["manner"][trial])
                self.height_seqs.append(data[day]["height"][trial])
                self.backness_seqs.append(data[day]["backness"][trial])
                self.roundedness_seqs.append(data[day]["roundedness"][trial])
                
                self.neural_time_bins.append(data[day]["sentenceDat"][trial].shape[0])
                self.phone_seq_lens.append(data[day]["phoneLens"][trial])
                self.articulatory_seqs_lens.append(data[day]["articulatoryLens"][trial])
                
                self.days.append(day)

    def __len__(self):
        return self.n_trials

    def __getitem__(self, idx):
        neural_feats = torch.tensor(self.neural_feats[idx], dtype=torch.float32)

        if self.transform:
            neural_feats = self.transform(neural_feats)

        return (
            neural_feats,
            
            torch.tensor(self.phone_seqs[idx], dtype=torch.int32),
            torch.tensor(self.voiced_seqs[idx], dtype=torch.int32),
            torch.tensor(self.place_seqs[idx], dtype=torch.int32),
            torch.tensor(self.manner_seqs[idx], dtype=torch.int32),
            torch.tensor(self.height_seqs[idx], dtype=torch.int32),
            torch.tensor(self.backness_seqs[idx], dtype=torch.int32),
            torch.tensor(self.roundedness_seqs[idx], dtype=torch.int32),
            
            torch.tensor(self.neural_time_bins[idx], dtype=torch.int32),
            torch.tensor(self.phone_seq_lens[idx], dtype=torch.int32),
            torch.tensor(self.articulatory_seqs_lens[idx], dtype=torch.int32),
            
            torch.tensor(self.days[idx], dtype=torch.int64),
        )
