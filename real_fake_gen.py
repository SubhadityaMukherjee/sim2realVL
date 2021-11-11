# %%
# from sim2realVL.data.rgbd_scenes import split_images_to_rgb_depth
# split_images_to_rgb_depth("/media/hdd/github/sim2realVL/sim2realVL/datasets/rgbd-scenes/datapath")

#%%
# sample = ds[1]
# print(sample)
# ds.show(1)

#%%

# # GENERATING FAKE DATA
# from sim2realVL.data.sim_dataset import SimScenesDataset
# from pathlib import Path
# from tqdm import tqdm
# import os

# main_path = Path("/media/hdd/Datasets/Sim2Real")
# gan_path_real = Path("/media/hdd/Datasets/Sim2Real/ganData/real")
# gan_path_fake = Path("/media/hdd/Datasets/Sim2Real/ganData/fake")
# ds = SimScenesDataset(images_path=str(main_path/"synthetic") , csv_path=str(main_path/"data.csv"))

# total_scenes = len(os.listdir(main_path/"synthetic"))
# for i in tqdm(range(1, total_scenes)):
    # ds.gen_images(i, gan_path_fake)


# GENERATING REAL DATA
from sim2realVL.data.rgbd_scenes import RGBDScenesDataset, RGBDObjectsDataset
from pathlib import Path
from tqdm import tqdm
import os

main_path = Path("/media/hdd/Datasets/Sim2Real")
gan_path_real = Path("/media/hdd/Datasets/Sim2Real/ganData/real")
gan_path_fake = Path("/media/hdd/Datasets/Sim2Real/ganData/fake")

ds = RGBDScenesDataset()

total_scenes = len(ds)
for i in tqdm(range(1, total_scenes)):
    ds.gen_images(i, gan_path_real)
