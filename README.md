# GANtasticFish

## 1. 개요
강아지, 고양이에 뒤이어 세 번째로 인기가 많은 애완동물은 물고기이지만, 커져가는 시장 규모에 반해 이들을 치료하고 관리하는 인프라가 제대로 갖추어져 있지 않다. 그 중 인기가 많은 종인 베타 물고기의 질병을 조기에 발견하고 대처할 수 있도록 딥러닝을 기반으로 한 베타 물고기 질병 자동 식별 모델을 구축하고자 한다.

## 2. 과제 수행 방법
### 2.1 데이터 수집 및 전처리
Google 이미지 검색 결과에 대한 Web Crawling 진행, 인터넷의 애완 물고기 동호회 사이트에 방문하여 이미지 수집
![bettafish](https://github.com/dusdnKR/GANtasticFish/assets/84877632/82d34f02-5d1f-400a-9798-c1aeae1636d9)

### 2.2 CNN 모델 생성 및 평가
Python 라이브러리인 ‘keras’를 활용하여 CNN 모델 생성.

+ Optimizer: adam

+ layer:  3

+ batch size: 32

+ epoch: 30

### 2.3 SinGAN 모델 사용

> #### 1) SinGAN model is required (link below)
>
> https://github.com/tamarott/SinGAN.git
>
>
> #### 2) Upload the original picture to the folder and enter the following command
```
%run main_train.py --input_name [file_name]
```

## 3. 결과
베타 물고기 original 이미지셋의 100장의 이미지를 모두 증강해 학습에 사용한 normal class와 tailrot class의 CNN 모델 기반 Image Classification의 경우 증강 전후에서 모델 정확도 성능 28.3% 향상이라는 유의한 성능 상승을 보임.
