네, 지금까지 진행했던 수업의 모든 내용을 마크다운으로 정리해 드리겠습니다.

# 1-1 수업 내용
- EDA
  - 데이터 통계 분석
  - 상관관계, 분포의 이해
- Scikit-learn (싸이킷런)
  - 싸이킷런 소개
  - 싸이킷런으로 표준화
  - 싸이킷런으로 학습한 모델 평가하기

# 1. EDA(Exploratory Data Analysis)가 무엇인가요?

- 데이터를 살펴보는 행동을 전부 EDA 라고 합니다!
- 예시
  - 음.. csv 파일이 있네, 한번 엑셀로 열어볼까? <--- EDA 입니다.
  - 음.. list 에 값들이 담겨있네, 한번 print로 출력해볼까? <--- EDA 입니다.
  - 값을 차트로 그려서 시각화된 데이터로 한번 살펴볼까? <--- EDA 입니다.
  - 데이터를 눈으로 보고 뭔가 생각을 했다? <----  EDA 입니다.

- 앞으로 여러분은 누군가 뭐하고 있냐 물어보면 EDA 하고 있다고 하시면 됩니다.
  - 데이터를 이해하려고 노력하는 행동들 모두 EDA 입니다.
  - 통계치를 출력해서 살펴보거나, 여러가지 차트로 규칙이나 특징을 눈으로 찾아보는것이죠.

### EDA에서 기본적으로 하는 일은 뭔가요?
- 거대한 데이터를 살펴볼때.. 일단 레코드 몇개 가볍게 살펴 볼 것 같아요.
- 그리고 데이터가 얼마나 거대한지 볼것이고...
- 어떤 Column들로 구성되어있는지 볼것 이고..
- 어떤 수치 값들이 있으면 여러가지 차트로 살펴보면서 데이터 이해를 해볼것 같습니다.

- 너무 당연한 말을 했지만, 실제 이론이 이렇습니다.
- EDA 작업은 주로 Pandas와 Seaborn으로 하는 것이 편리합니다.

# 2. EDA를 할 데이터셋 이해하기
- seaborn 에서 제공하는 연습용 데이터 셋인 **mpg** 가 있습니다.
- 차량별 연비 정보가 나와있는 데이터셋이고, mpg는 mile per gallon (갤런당 몇 마일 갈 수 있는가?.. 즉 연비) 입니다.
- 차량 정보도 함께 나와있습니다.

```python
import seaborn as sns

# seaborn 내장 데이터 셋 불러오기 (데이터 프레임)
df = sns.load_dataset("mpg")

df.head()

#df.head(10) # 10개 출력
#df.tail(300) #마지막 5개 출력
데이터 크기, Column 확인
데이터 크기 및 Column이 뭐가 있는지 있는지 살펴봅시다.
데이터프레임 Info... --> df.info() 하나면 됩니다. EDA는 역시 Pandas!
import seaborn as sns
df = sns.load_dataset("mpg")

df.info()
여기서 Non-Null Count가 있습니다.
결측치(값이 누락된 것, Missing Value)가 몇개인지 알 수 있습니다.
잘 보면 horsepower(마력) 필드에서 6개 결측치가 있다는 뜻이죠.
데이터 통계 확인
통계 확인 이라고, 데이터들 요약 정보를 보는 겁니다.
데이터 프레임 describe() --> df.describe() 로 확인할 수 있습니다.
import seaborn as sns
df = sns.load_dataset("mpg")

df.describe()
count는 결측치 아닌 것 개수.. 아까 마력이 6개 없었죠?
평균은 데이터가 전체적으로 어느 정도 값인지 한 눈에 알수 있는 중요한 데이터죠
예시 : 고등학교 1반의 평균은 80점이네? 2반은 85점인데 말이지... 2반이 공부를 더 잘하는 군
표준편차, 기억나실까요?
기억이 안난다면 암기하세요! 표준편차 : 평균에 얼마나 퍼져있는지를 나타냅니다.
표준편차가 값이 크면.. 편차가 심하네~ 라고 생각하면 됩니다.
표준편차가 값이 작으면.. 편차가 없고 평균에 몰려있네? 라고 생각하면 됩니다.
표준편차 예시
1반 표준편차는 값이 크네? 그런데 평균은 80이고 하니까.. 성적 매우 낮은 친구가 존재하겠군!!
2반 표준편차 값이 작네? 공부를 심하게 못하는 친구가 없나 보군.
min값과 max은 이상치가 있는지 살펴보기 좋습니다.
이상치 : 데이터 범위에서 많이 벗어난 값
25%, 50%, 75% 값은 데이터 분포를 갸늠할수 있습니다.
3. mpg 데이터에서 상관관계 찾기
상관관계가 무엇인지 알기 전에, 실제 mpg가 무슨 데이터인지 살펴보겠습니다.
상관관계란?
일상생활 속에서 상관있어? 없어? 라는 말 자주 들으셨죠? 바로 그 '상관' 입니다.
예시
(와이프에게) 내가 일하다 늦게 오는 거랑, 너의 혈압이랑 무슨 상관이 있어?
(의사선생님에게) 제가 제로 콜라 많이 먹는데, 고혈압하고 상관 있나요?
통계에서 한 변수가 변할 때, 다른 변수가 함께 변하면 상관관계 가 있다고 합니다.
더 정확하게는 X, Y 가 얼마나 선형 관계를 갖는가? 라는 정의가 있지만 생략합니다!
상관관계를 찾기 위한 시각화 1
무게와 가속도는 상관관계가 있을 것으로 느껴집니다.
제 느낌입니다.
제 경험상, 무거운 사람은 달리기 가속도가 느렸거든요.
시각화를 통해 acceleration 변수(제로백)와 weight 변수가 상관관계가 있는지 살펴봅시다.
제로백 : 0에서 100m 까지 도달하는데 걸리는 시간(초)
import seaborn as sns
df = sns.load_dataset("mpg")

sns.scatterplot(data=df, x="weight", y="acceleration", alpha=0.7)
print()
뭔가 느낌이 옵니다. weight가 무거울수록 제로백이 낮아지는 것 처럼 보입니다.
제로백이 수치가 낮다는 것은 100m 까지 도달하는데 금방 걸린다는 뜻입니다.
선형회귀선을 추가해봅시다. (regression plot)
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("mpg")

sns.regplot(data=df, x="weight", y="acceleration", scatter_kws={'alpha':0.6})
#print()
두 변수가 얼마나 상관이 있는지, 수치로 출력하고 싶습니다. 이를 상관계수(Correlation coefficient)라고 합니다.
상관계수는 -1 ~ 1 사이의 값을 갖습니다.
값 예시
+1 : 완전한 양의 상관관계, 무조건 같이 오름 (무게 UP시, 가속도 UP)
+0.7 : 강한 양의 상관관계, 거의 같이 오름
0 : 상관없음
-0.7 : 강한 음의 상관관계, 거의 반대로 동작
-1 : 완전한 음의 상관관계, 무조건 반대로 동작 (무게 UP시, 가속도 Down)
상관계수를 출력하면.. 아마 음의상관관계로 나오겠죠?
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("mpg")

# 상관계수 값 계산
corr = df["weight"].corr(df["acceleration"])

print(f'상관계수(Correlation coefficient)')
print(corr)
4. 상관관계를 확인하는 EDA 방법 - 히트맵
각 변수별로 상관관계를 한눈에 파악할 수 있습니다.
양의 상관계수가 높은 값 or 낮은 값을 찾으면 돼죠.
import numpy as np
import seaborn as sns

df = sns.load_dataset("mpg")

# 상관계수 행렬 계산
corr = df.corr(numeric_only=True)

# 히트맵 출력
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=1)
print()
복잡해 보입니다.
자세히 보면 중복 데이터들이 있네요. 대칭되어있습니다.
불필요한데이터를 삭제해봅시다.
import numpy as np
import seaborn as sns

df = sns.load_dataset("mpg")

# 상관계수 행렬 계산
corr = df.corr(numeric_only=True)

# 삼각형 마스크 만들기 (상단 삼각형 가리기)
mask = np.triu(np.ones_like(corr, dtype=bool))

# 히트맵 출력
sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", linewidths=1)
print()
아주 강력하게 상관관계를 보이는 것은 진한 파랑색과 진한 빨강으로 잘표시가 되네요.
신기한 점이 몇 가지 있네요.
model year이 올라갈수록 연비가 점점 올라가는 추세군요?
model year가 올라갈수록 무게가 가벼워진다. 년식이 높을 수록 차량 무게가 가벼워 진다로 볼 수 있겠네요.
제로백 (100m 까지도달 시간, acceleration)은 weight 보다는 마력이 중요하네요.
weight 는 왜 상관관계가 있을까요?
weight 와 관계가 된 속성을 보면 마력, 기통, 배기량이 강한 상관 관계를 갖고 있네요.
무게가 무거울 수록 큰 힘을 발휘해서 제로백이 낮아지고 있다고 봐도 되겠네요.
5. 분포(Disribution)
이 분포는 고등학교때 배운 개념입니다~ (기억이 잘 안날 확률이 더 높다고 생각합니다.)
이 개념을 복습하면서, 싸이킷런으로 데이터의 분포, 분산 정도를 확인해봅시다.
분포가 뭔가요?
분포는 어느 값에 몰렸나?.. 어느 값이 인기가 많나.. 를 확인할 수 있습니다. (암기하세요)
분포의 정의는 데이터가 퍼져있는 모양 입니다.
롯데월드에서 어느 놀이기구에 몰렸는지 보려면, 분포를 보면 되겠죠?
분포를 확인하는 방법은, 값 마다 빈도수(Frequency)를 확인하면 한눈에 알 수 있습니다.
어디에 몰렸는지 바로 볼 수 있죠.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("mpg")

# bins = 20 --> 20개 단위로 결과를
# kde = True --> 분포 곡선(선) 출력
sns.histplot(df["weight"], bins=20, kde=True, color="skyblue")
print()
위 데이터를 보니, 차량 무게는 2,000 파운드 (약 900KG) 에 가장 몰려있군요.
분포의 오해! [중요]
분포는 통계량... 수치가 아닙니다. 모양입니다.
수 하나로 분포 모양을 설명 못해요.
분포 모양을 설명하려면, 여러 통계 값으로 표현합니다. (아래는 수치로 표현되는 통계량 들입니다.)
평균 : 중심이 어디인가
분산 : 평균 주변으로 얼마나 퍼져있나?
표준편차 : 퍼짐의 강도
왜도 : 왼쪽과 오른쪽 어느쪽으로 값이 치우쳐있나?
첨도 : 가운데가 뾰족한가, 납작한가...
위 5개의 통계량으로도 분포(모양)을 정확히 설명할 수 없지만, 분포의 특징을 수치로 표현할 순 있죠.
[참고] AI에서 자주 사용하는 통계량은 --> 평균과 표준편차!
평균과 표준편차.. 이 두 가지를 가장 많이 씁니다.
어디에 쓰이는지 느낌만 알고 넘어갈게요.
심하게 큰 값이 있으면, 작은 값을 가진 변수가 학습이 잘 안되거든요.
입력 데이터를 특정 평균의 표준편차 값을 가진데이터로 스케일링하면 학습이 더 잘됩니다.
값의 범위를 좁히거나 늘리는 거죠.
그래서 데이터 전처리 작업으로, 필수처럼 합니다.
데이터를 특정 기준에 맞춰 스케일링 하는 개념을 "정규화" 라고 합니다.
정규화 중에서 평균 0, 표준편차 1 으로 정규화하는 것을 표준화 라고 합니다.
표준화는 곧 다룰 겁니다. 이를 위해 분산에 대해 완벽히 이해해주세요.
6. 분산
지금까지 분포가 뭔지 알아봤습니다. 이번엔 '분산'에 대해 얘기해보겠습니다.
분포는 퍼져있는 모양이고, 어디에 쏠려있는지 눈으로 볼 수 있죠.
분포를 수치로 설명하는 통계량 중 하나가 바로 분산 입니다.
분산은 평균 기준으로 얼마나 퍼져있는지를 수치로 나타냅니다.
분산 개념은 꼭 알아야합니다.
AI 에서 평균, 표준편차.. 이렇게 2개를 많이쓴다고 했잖아요?
표준편차를 분산으로 계산합니다. 제곱근만 하면 바로 표준편차예요.
분산의 예시
A반과 B반이 모두 평균이 80점 이라고 가정하겠습니다.
A 반 (총 3명) : 79점, 80점, 81점
B 반 (총 3명) : 70점, 80점, 90점
A반은 분산이 작습니다.
B반은 분산이 큽니다.
분산 계산법
평균의 차이들을 제곱해서 평균하면 됩니다.
import numpy as np

data = np.array([79, 80, 81])
variance = np.var(data) # 분산

print(variance)
이번엔 [70, 80, 90] 의 분산값을 구해보시죠.
import numpy as np

data = np.array([70, 80, 90])
variance = np.var(data) # 분산

print(variance)
정리하자면.. 분산값이 크면 평균에서 퍼저있는 정도가 큰것입니다.
7. 한방에 EDA 를 하자! 한방 차트 - pairplot()
EDA 할때 상관관계를 히트맵으로 볼 수 있었습니다.
양의 상관관계 / 음의 상관관계 / 상관없는 변수를 구분할 수 있었죠.
EDA 할때 어디에 값이 몰려있는지, 모양을 보고싶을 때 분포를 확인하면 됩니다.
빈도수를 막대 차트로와 선으로 표현하면 분포(모양)을 확인할 수 있었죠.
위 내용들을 한방에 볼 수 있는 plot이 있습니다. pairplot 입니다.
아래 데이터를 이해해보세요.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("mpg")

# 마력에 결측치 제거 (pairplot은 결측치(NaN)값 있으면 에러 납니다.)
df = df.dropna(subset=["horsepower"])

# pairplot 시각화
# corner : 아랫쪽 삼각형만 그림
# kind : 변수 쌍의 관계를 나타내는 플롯의 종류를 지정 (reg: regression으로 산점도와 회귀선을 함께 그려줌)
sns.pairplot(df[["weight", "horsepower", "acceleration"]], corner=True, kind="reg", plot_kws={'line_kws': {'color': 'red'}})
#print()
8. EDA 끝!, 정리합시다.
EDA는 데이터를 이해하고 분석하는 과정입니다.
오해하면 안되는 것이 있는데요. 데이터를 수정하거나 전처리 하는 과정이 아닙니다!
이상치와 결측치를 확인하는 것 = EDA
이상치와 결측치를 제거하거나 다른 값으로 채우는 행동 = EDA가 아닙니다. 전처리 과정이죠.
단순히 데이터를 출력해보는 것도 EDA 이니까.. EDA는 정말 쉽죠.
EDA 수업을 통해 변수, 분포, 상관관계, 상관계수, 분산 등 필수 통계 지식을 이해하면 됩니다.
9. Scikit-learn 이란?
드디어 새로운 챕터로 넘어왔습니다.
머신러닝 Library가 정말 많지만, 머신러닝 모델을 다루는 대표적인 Library는 다음과같습니다.
Scikit-Learn : 머신러닝 대표 라이브러리
TensorFlow : 머신러닝 중 딥러닝에 특화된 라이브러리
PyTorch : 머신러닝 중 딥러닝에 특화된 라이브러리 (코드 간결성이 더 높음)
머신러닝 모델은 선형회귀, 로지스틱회귀, 클러스터링, 신경망 등 많거든요.
딥러닝은 신경망(Neural Network, 줄여서 NN)을 수십 층으로 딥~ 하게 만든 모델을 의미합니다. (몇 층인지 기준은 없어요.)
다시 말하면.. 싸이킷 런은 머신러닝 Library / PyTorch는 딥러닝 Library 입니다.
10. Scikit-learn 기본 코드 이해 (선형회귀, 로지스틱회귀)
싸이킷런의 Hello world인 선형회귀 모델을 써봅시다.
싸이킷 런의 입력 데이터는 2차원 행렬로 입력 받습니다.
따라서 입력데이터 X를 2차원 행렬로 변경합니다.
reshape(n, 1) : 세로 n x 가로 1 사이즈로 행렬 형태 변경
n을 소스코드에서는 -1로 표현합니다.
Library 를 쓰니까, 저번에 직접 구현했던 것 보다 코드가 확실히 간결합니다.
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 데이터 불러오기
tips = sns.load_dataset("tips")
X = tips["total_bill"].values.reshape(-1, 1)  # 2차원으로 변환, -1 은 'n' 이라는뜻 입니다.
y = tips["tip"].values

# 모델 생성 및 학습
model = LinearRegression() # 아직 학습 안된 모델객체 생성
model.fit(X, y) #X, y로 학습시작 (내부적으로 GD 안하고 정규방정식으로 한방에 최적 a, b를 계산함)

# 예측
y_hat = model.predict(X)

# 시각화
plt.scatter(X, y, color='blue', alpha=0.6, label='Actual Data')
plt.plot(X, y_hat, color='red', linewidth=2, label='Regression Line')

plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Linear Regression: Total Bill vs Tip")
plt.legend()
plt.show()
이번엔 로지스틱 회귀입니다
저번에 직접 짰던 코드를 Library를 쓴 코드로 바꿔보겠습니다
특이한 점은 model.predict_proba( ) 호출 시 탈락확률과 합격확률이 동시에 함께 반환됩니다.
예를들면 f(2시간) = [탈락확률 30%, 합격확률 70%] 이렇게요.
차트는 합격확률만 그리기 위해 "합격확률"만 추출해서 선으로 그렸습니다.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 공부 시간 (입력값)
X = np.array([1,2,3,4,5,6,2,3,4,5,6,7,1,2,3,4,5,6,7,8,2,3,4,5,6,7,8,9,10]).reshape(-1, 1)

# 합격 여부 (출력값)
y = np.array([0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1])

model = LogisticRegression()
model.fit(X, y)

X_new = np.linspace(0, 11, 200).reshape(-1, 1) # 0~11시간까지 세밀하게
y_hat = model.predict_proba(X_new) # [탈락확률, 합격확률]
y_hat = y_hat[:, 1] # 합격 확률만 추출

plt.figure(figsize=(8, 5))
plt.plot(X_new, y_hat, color='red', linewidth=2)
plt.xlabel("Study Time")
plt.ylabel("Pass Probability")
plt.grid(True)
print()
11. 표준화 (전처리)의 필요성
데이터를 평균 0, 표준편차 1 형태로 바꾸는 전처리 입니다.
전처리 작업을 하는 첫 번째 이유
아래와 같은 데이터가 있습니다.
변수 1 : 키 160 ~ 190 cm 범위
변수 2 : 손톱 길이 0.5cm ~ 1.5cm 범위
위 원본값을 그대로 학습하면 키 때문에 손톱 데이터가 묻혀요.
그래서 아래와 같이 바꿔주면 학습 오작동을 막을 수 있습니다.
전처리 후 변수 1 : 키 0 ~ 1 범위
전처리 후 변수 2 : 손톱 길이 0 ~ 1 범위
전처리 작업을 하는 두 번째 이유
표준편차 1이 되도록 데이터를 조율 하는 이유입니다.
값 자체만 보면 다른 값과 비교가 안된 원본 값 그대로입니다.
평균에서 얼만큼 벗어난 값인지 수치로 변환하면, 상대적인 값을 확인할 수 있습니다.
예시
원본 값 : [32점, 99점, 15점, 38점, 39502점]
전처리 후 : [하위 2%, 상위 44%, 하위1%, 하위 2.3%, 상위 0.1%]
전처리 후 데이터로 학습하면, GD 학습이 더 잘됩니다.
꼭 평균 0, 표준편차 1로 학습해야하나요?
아니요. 별 이유없으면 표준화(평균0, 표준편차1)로 하구요.
수학 계산상 더 학습이 잘되는 좋은 평균과 표준편차값이 발견되면 다른 값으로 합니다.
모델마다 정규화를 어떤 평균값과 어떤 표준편차 값으로 하는지 차이가 있습니다.
입력 데이터에 따라서 AI 학자들이 값을 결정하곤 합니다.
정규화와 표준화 차이가 뭔가요?
정규화는 값의 범위를 조율하는 행동 자체를 말합니다.
표준화는 "평균 0, 표준편차 1"로 정규화 하는 것을 말합니다.
표준화는 정규화 행동 중 하나입니다.
12. 표준화 구현하기
표준화는 StandardScaler 라는 클래스가 싸이킷런에 준비되어있습니다.
표준화 하는 변환 수식이 있지만 생략합니다~!
표준화를 통해 원본 데이터의 특성은 최대한 가져가면서, 학습이 더 잘되도록 값이 변경되는 것입니다.
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

tips = sns.load_dataset("tips")

X = tips["total_bill"].values.reshape(-1, 1)  # 2차원으로 변환 (n, 1)
y = tips["tip"].values.reshape(-1, 1)

# 표준화를 해주는 객체만 생성
scaler_X = StandardScaler()
scaler_y = StandardScaler()

# 표준화 하기
scaler_X.fit(X) # fit : 평균과 표준편차 계산하여 내부 변수에 저장해둠
scaler_y.fit(y)
X_std = scaler_X.transform(X) # 변환 (변환 수식에 원본의 평균과 표준편차 값이 필요)
y_std = scaler_y.transform(y)

# sub plot (1 x 2로 2개의 차트로 출력 준비)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 왼쪽 차트 (원본)
axes[0].scatter(X, y, color='blue', alpha=0.6)
axes[0].set_title("Before Standardization")
axes[0].set_xlabel("Total Bill ($)")
axes[0].set_ylabel("Tip ($)")

# 오른쪽 차트 (표준화 이후)
axes[1].scatter(X_std, y_std, color='red', alpha=0.6)
axes[1].set_title("After Standardization")
axes[1].set_xlabel("Total Bill (Standardized)")
axes[1].set_ylabel("Tip (Standardized)")
print()
scaler_X.transform(X) 코드는 표준화 객체인 scaler_X를 사용하여 데이터 X를 실제로 표준화된 값으로 변환하는 역할을 합니다.

이전에 scaler_X.fit(X)를 통해 scaler_X 객체는 데이터 X의 평균과 표준편차를 계산하여 내부적으로 저장해 두었습니다.

transform(X) 메서드는 저장된 평균과 표준편차를 사용하여 X의 각 데이터 포인트에 대해 다음과 같은 표준화 변환 수식을 적용합니다.

$$ z = \frac{x - \mu}{\sigma} $$$$ z = \frac{x - \mu}{\sigma} $$

여기서:

$x$$x$는 원본 데이터의 값
$\mu$$\mu$는 fit() 단계에서 계산된 평균
$\sigma$$\sigma$는 fit() 단계에서 계산된 표준편차
$z$$z$는 표준화된 값
이렇게 변환된 X_std 데이터는 평균이 0, 표준편차가 1에 가까운 분포를 갖게 됩니다. 이 과정은 모델 학습 시 데이터의 스케일 차이로 인한 문제를 줄여 학습 성능을 향상시키는 데 도움을 줍니다.

13. 표준화한 데이터로 선형회귀하기
우리 목적은 다음과 같습니다.
데이터를 표준화 한 후에 학습합시다.
이후 예측을 해봅시다.
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

tips = sns.load_dataset("tips")

X = tips["total_bill"].values.reshape(-1, 1)
y = tips["tip"].values.reshape(-1, 1)

scaler_X = StandardScaler()
scaler_y = StandardScaler()

scaler_X.fit(X) # fit : 평균과 표준편차 계산하여 내부 변수에 저장해둠
scaler_y.fit(y)
X_std = scaler_X.transform(X) # 변환 (fit을 해야 변환 가능)
y_std = scaler_y.transform(y)

# 선형회귀 모델 학습
model = LinearRegression()
model.fit(X_std, y_std)

# 예측
y_hat_std = model.predict(X_std)

# 예측 후 원본값으로 복원
y_hat = scaler_y.inverse_transform(y_hat_std)

# 시각화
plt.figure(figsize=(7,5))
plt.scatter(X, y, color='blue', alpha=0.6, label='Actual data')
plt.plot(X, y_hat, color='red', linewidth=2, label='Regression line')
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Linear Regression")
plt.legend()
plt.show()
이제 예측을 해봅시다.
$50 어치 식사한 손님이 어느 정도 TIP을 낼지 예측해봅시다.
표준화를 한 데이터로 만든 모델이므로, 예측할때도 입력 데이터를 표준화 한 후 입력해야한다는 것을 잊지마세요.
new_bill = [[50]]
new_bill_std = scaler_X.transform(new_bill) # 표준화

# 예측하기
pred_tip_std = model.predict(new_bill_std) # 모델 예측 전, 입력 데이터 표준화 필수!!

# 예측값은 평균 0, 표준편차 1 에 맞춘 값이 나왔음. 다시 원상복구
pred_tip = scaler_y.inverse_transform(pred_tip_std)

# 결과 출력
print(f'$50 식사한 손님의 예상 TIP : {pred_tip}')
14. 모델평가하기
선형회귀를 생각해보면 y = ax + b 에서, MSE가 가장 낮은 a, b 를 찾는 노력을 해왔습니다.
이렇게 완성된 선형회귀 모델이 처음보는 데이터에 얼마나 예측을 잘하는지? 평가를 하는 여러가지 방법이 있습니다.
모델을 평가하는 이유
모델 평가하는 이유는 단순히, 어떤 모델이 더 좋은 모델인가? 를 가리기 위함이 아닙니다.
학습 도중에 중간 평가를 하여, 학습을 조율하기 위함입니다. (더 나은 학습을 위해)
예시)
학원 6개 다니면서 학습중인 우리아이는 "4세 고시" 평가 이후에 학원을 2개 더 늘리기로 했습니다~!
평가를 위해 데이터를 나누는 방법
우리 실습에서는 데이터셋을 몽땅 학습용으로 사용했습니다.
평가를 하려면, 학습에 사용하지 않은 데이터로 평가를 해야합니다.
일반적인 AI 학습에서는 전체 데이터를 3개의 데이터로 나누는 것이 일반적입니다.
Train Set
학습용 데이터로 80% 정도 사용합니다.
Validation Set
검증용 데이터, 학습 중간 중간 평가를 하여 학습 방법을 조율합니다.
Validation Set 결과로 학습률(lr.. 점프거리)를 조율하거나 학습을 중단하기도 합니다.
예시
'4세 고시' 결과 진도를 더 빼기로 했습니다.
오은영 박사님 검사 결과 학원을 전부 그만두기로 했습니다.
Test Set
처음보는 데이터로 모델을 평가합니다. (수능점수)
싸이킷 런으로 데이터 나누기
선형회귀에서는 Validation Set 까지 필요하진 않습니다.
나중에 신경망 모델 에서 필요하긴합니다.
간단히 싸이킷 런으로 Train Set과 Test Set을 분리하는 방법을 알아 봅시다.
싸이킷런의 train_test_split 함수를 사용합니다.
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

tips = sns.load_dataset("tips")
X = tips["total_bill"].values
y = tips["tip"].values

print(f'원본 개수 : {X.size}개')

# 데이터를 2개로 분리
# X_train, Y_train = 0.8 (80%)
# X_test, Y_test = 0.2 (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 랜덤으로 섞어줌

print()
print(f'[분할 후] Train 데이터 수 : {X_train.size}개')
print(f'[분할 후] Test 데이터 수 : {X_test.size}개')
나중을 위해서 한번 3개로 분리를 해봅시다.
Train = 80%, Validation = 10%, Test = 10%
import seaborn as sns
from sklearn.model_selection import train_test_split

tips = sns.load_dataset("tips")
X = tips["total_bill"].values
y = tips["tip"].values

print(f'원본 개수 : {X.size}개')

# 1차 분할 : Train (80%), 임시 나머지 (20%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)

# 2차 분할 : Validation (10%), Test (10%)
# 전체의 20% 중 절반(=0.5)씩 나눠서 10%, 10%
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 개수 출력
print()
print(f'[분할 후] Train 데이터 수 : {X_train.size}개 (약 80%)')
print(f'[분할 후] Validation 데이터 수 : {X_val.size}개 (약 10%)')
print(f'[분할 후] Test 데이터 수 : {X_test.size}개 (약 10%)')
선형회귀 모델에서 대표적인 평가지표
MSE와 R²이 있습니다.
MSE
오차의 제곱한 값들의 평균입니다.
0에 가까울수록 성능이 가장 좋습니다.
Loss(Error)를 계산할 때도 쓰이지만, 모델을 평가할 때도 쓰일수 있습니다.
R²(결정계수)
모델이 데이터의 흐름을 잘 예측하고 있는지 평가합니다.
결과는 0 ~ 1 값인데, 1에 가까울수록 성능이 좋습니다.
상세한 내용은 Easy 교안에서 다루지 않습니다.
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score #MSE, R²

tips = sns.load_dataset("tips")
X = tips["total_bill"].values.reshape(-1, 1) # 2차원 행렬로 변환 (n x 1)
y = tips["tip"].values

# Train / Test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습 (Train 데이터 사용)
model = LinearRegression()
model.fit(X_train, y_train)

# 예측 (Test 데이터 사용)
y_pred = model.predict(X_test)

# 모델 평가
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"MSE (평균제곱오차): {mse:.4f}")
print(f"R²(결정계수): {r2:.4f}")
로지스틱 회귀에서 대표적인 평가 지표
Accuracy, F1-score, AUC 가 있습니다.
참고로 크로스엔트로피는 Loss 함수로는 자주 쓰이지만, 평가용으로 쓰기에는 출력값을 설명하기 모호하여 사용하지 않습니다.
Accuracy(정확도)
전체 테스트 데이터 중에 모델이 정답을 얼마나 맞췄는지 비율입니다.
결과는 0 ~ 1 값인데, 1에 가까울수록 성능이 좋습니다.
상세한 내용은 Easy 교안에서 다루지 않습니다.
F1-score
모델이 정확히 1(합격)이라고 맞춘 것과, 1을 놓치지 않은 것의 비율입니다.
결과는 0 ~ 1 값인데, 1에 가까울수록 성능이 좋습니다.
상세한 내용은 Easy 교안에서 다루지 않습니다.
AUC (ROC-AUC)
모델이 0(탈락)과 1(합격)을 잘 구분하는 정도를 나타냅니다.
결과는 0 ~ 1 값인데, 1에 가까울수록 성능이 좋습니다.
0인데 1로 잘못된 예측을 한것과, 실제 1로 맞춘 비율을 선으로 그렸을 때 아래 면적 크기를 나타냅니다.
상세한 내용은 Easy 교안에서 다루지 않습니다.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import train_test_split

# 데이터 준비
X = np.array([1,2,3,4,5,6,2,3,4,5,6,7,1,2,3,4,5,6,7,8,2,3,4,5,6,7,8,9,10]).reshape(-1, 1)
y = np.array([0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1])

# Train / Test 분리 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 생성 및 학습 (Train 데이터 사용)
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측 (Test 데이터사용)
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]  # 불합격 확률 버리고, 합격 확률만 추출

# 평가 지표 계산
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_prob)

# 결과 출력
print(f'Accuracy : {acc:.4f}')
print(f'F1-score : {f1:.4f}')
print(f'AUC: {auc:.4f}')
15. 끝으로
수고 많으셨습니다!
이 수업에서는 EDA 분석을 하면서, 동시에 통계 기본 지식을 다루었습니다.
또한 싸이킷런 Library를 사용해보면서, 표준화와 모델 평가에 대한 기본 지식을 다루었습니다.
이 지식은 앞으로 딥러닝을 배울 때 기반 지식이 될 것입니다.
딥러닝은 AI의 핵심이죠.
아시겠지만, AI 학습 내용은 총 3개로 분류될 수 있습니다.
Easy 자료 (강사님 자료)
AI를 처음 공부하는 분들을 위해 만들어져있습니다.
내용을 모두 이해해야합니다! 강사님의 도움을 적극적으로 받아주세요.
실습 / 과제 자료 (업스테이지 자료)
AI를 공부해본 경험자 위주로 만들어져있습니다.
퍼즐조각을 모은다는 생각으로 공부해주세요!. GPT의 도움을 적극적으로 받아주세요.
교수님 강의
국내 최고의 AI 교수님들의 강의가 시작됩니다.
최대한 내용을 이해해봅시다.