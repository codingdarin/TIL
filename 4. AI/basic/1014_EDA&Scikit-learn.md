# EDA & Scikit-learn 기초

## 1. EDA(Exploratory Data Analysis)

### EDA란?
- 데이터를 살펴보고 이해하려는 모든 행동
- 예시: 데이터 파일 열어보기, 값 출력하기, 시각화하기 등

### EDA 기본 작업
- 샘플 데이터 확인
- 데이터 크기 파악
- 컬럼 구조 파악
- 통계 수치 확인 및 시각화

### 주요 도구
- **Pandas**: 데이터 조작 및 분석
- **Seaborn**: 통계적 시각화

---

## 2. MPG 데이터셋 탐색

### 데이터 불러오기
```python
import seaborn as sns

df = sns.load_dataset("mpg")
df.head()  # 상위 5개 레코드 확인
```

### 데이터 정보 확인
```python
df.info()  # 크기, 컬럼, 결측치 확인
```
- **Non-Null Count**: 결측치가 아닌 값의 개수
- horsepower 필드에 6개 결측치 존재

### 기술 통계량 확인
```python
df.describe()
```

**주요 통계량**
- **count**: 결측치 아닌 데이터 개수
- **mean**: 평균값 (데이터의 중심 경향)
- **std(표준편차)**: 평균으로부터 데이터가 얼마나 퍼져있는지
  - 크면: 편차가 심함 (극단값 존재 가능)
  - 작으면: 평균 근처에 집중
- **min/max**: 이상치 탐지에 유용
- **25%, 50%, 75%**: 데이터 분포 파악 (사분위수)

---

## 3. 상관관계 분석

### 상관관계란?
- 한 변수가 변할 때 다른 변수도 함께 변하는 관계
- 두 변수 간의 선형 관계 정도를 나타냄

### 산점도로 상관관계 확인
```python
sns.scatterplot(data=df, x="weight", y="acceleration", alpha=0.7)
```

### 회귀선 추가
```python
sns.regplot(data=df, x="weight", y="acceleration", scatter_kws={'alpha':0.6})
```

### 상관계수 계산
```python
corr = df["weight"].corr(df["acceleration"])
print(corr)  # -0.417 (음의 상관관계)
```

**상관계수 해석**
- **1에 가까움**: 강한 양의 상관관계
- **0에 가까움**: 상관관계 없음
- **-1에 가까움**: 강한 음의 상관관계

---

## 4. 히트맵으로 전체 상관관계 파악

```python
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=1)
```
- 모든 변수 간 상관계수를 색상으로 표현
- 한눈에 강한 상관관계 파악 가능

---

## 5. Pairplot - 종합 시각화

```python
sns.pairplot(df)
```

**특징**
- 대각선: 각 변수의 분포(히스토그램)
- 비대각선: 변수 간 상관관계(산점도)
- 숫자형 데이터만 시각화
- 데이터 많으면 시간 오래 걸림

---

## 6. Scikit-learn 소개

### 개요
- 머신러닝을 위한 파이썬 라이브러리
- 데이터 전처리, 모델 학습, 평가 등 제공
- 딥러닝 시대에도 여전히 필수적

### 주요 기능
- 데이터 전처리
- 머신러닝 모델 구현
- 모델 성능 평가
- 하이퍼파라미터 튜닝

---

## 7. 표준화(Standardization)

### 표준화란?
- 데이터의 평균을 0, 표준편차를 1로 변환
- 서로 다른 스케일의 데이터를 비교 가능하게 만듦

### 표준화 공식
```
z = (x - μ) / σ

- x: 원본 데이터
- μ: 평균
- σ: 표준편차
- z: 표준화된 값
```

### 표준화가 필요한 이유
- 머신러닝 모델은 데이터 스케일에 민감
- 특정 변수가 과도하게 영향을 주는 것 방지
- 모델 학습 속도 및 성능 향상

---

## 8. StandardScaler 실습

```python
from sklearn.preprocessing import StandardScaler
import pandas as pd

# 결측치 제거
df.dropna(inplace=True)

# 숫자형 컬럼 선택
numeric_cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']
df_numeric = df[numeric_cols]

# StandardScaler 객체 생성
scaler = StandardScaler()

# 표준화 수행
df_scaled = scaler.fit_transform(df_numeric)

# DataFrame으로 변환
df_scaled = pd.DataFrame(df_scaled, columns=numeric_cols)
```

### 표준화 확인
```python
df_scaled.describe()
```
- mean ≈ 0 (거의 0)
- std ≈ 1 (거의 1)

---

## 9. 모델 평가 지표

### 회귀 모델 평가

**MSE (Mean Squared Error)**
- 예측값과 실제값 차이의 제곱 평균
- 오차가 클수록 큰 패널티
- 작을수록 좋은 모델

**RMSE (Root Mean Squared Error)**
- MSE에 루트를 씌운 값
- 원본 데이터와 동일한 단위
- 해석이 더 직관적

```python
from sklearn.metrics import mean_squared_error
import numpy as np

y_true = [1, 2, 3, 4, 5]
y_pred = [1, 2, 4, 4, 6]

mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

print(f'MSE: {mse}')   # 0.6
print(f'RMSE: {rmse}') # 0.775
```

### 분류 모델 평가

**Accuracy (정확도)**
- 전체 중 올바르게 예측한 비율
- 가장 직관적이지만 불균형 데이터에서는 부적합

**F1-score**
- 정밀도와 재현율의 조화평균
- 불균형 데이터에서도 적절한 평가 가능
- 0~1 사이 값, 1에 가까울수록 좋음

**ROC-AUC**
- ROC 곡선 아래 면적
- 0.5: 랜덤 예측 수준
- 1.0: 완벽한 분류
- 0~1 사이 값, 1에 가까울수록 좋음

```python
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

y_true = [0, 1, 1, 1, 0]
y_pred = [0, 1, 0, 1, 0]

acc = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
auc = roc_auc_score(y_true, y_pred)

print(f'Accuracy: {acc:.4f}')  # 0.8333
print(f'F1-score: {f1:.4f}')   # 0.8889
print(f'AUC: {auc:.4f}')        # 0.5000
```

---

## 핵심 요약

1. **EDA는 데이터 이해의 첫 단계** - 통계량 확인과 시각화가 핵심
2. **표준편차가 크면** 데이터가 평균에서 많이 퍼져있음
3. **상관계수**: -1~1 사이 값, 0에 가까우면 상관관계 없음
4. **표준화**: 머신러닝 모델 성능 향상을 위한 필수 전처리
5. **평가지표 선택**: 회귀는 MSE/RMSE, 분류는 상황에 따라 Accuracy/F1/AUC