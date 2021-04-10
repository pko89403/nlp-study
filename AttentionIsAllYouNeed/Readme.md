# Abstract
- 시퀀스 변환 모델은 RNN과 CNN에 기반한 인코더와 디코더 기반의 모델이 지배적이었다.
- 가장 좋은 성능을 보이는 모델은 어텐션으로 인코더와 디코더를 연결한 모델이 었다.
- 트랜스포머라는 어텐션에 전적으로 기반하고 RNN과 CNN을 버리는 간단한 네트워크 구조를 제시한다.
- 병렬 처리가 가능하고 학습 시간을 적게 사용하는 훌륭함을 실험으로 보인다.
- 3.5일 간 8 GPU에서 학습으로 싱글 모델로 SOTA BLEU 스코어를 보인다.
- 다른 태스크에 대한 일반화와 그리고 거대한 학습 데이터와 제한된 학습 데이터에서도 훌륭했음을 보인다.
# 1. Introduction
- RNN 모델은 일반적으로 입력 심볼의 위치와 출력 심볼의 위치에 따라서 요소 연산을 한다.
- RNN의 내재된 시퀀셜한 특성은 학습 예제의 병렬화를 배제한다.
- Attention은 시퀀스 모델링과 시퀀스 변환 모델을 구성하는 필수적인 부분이 되었다.
    - 입력과 출력 시퀀스의 거리에 의존하지 않고 모델링이 가능하다.
- Transformer는 Recurrent를 피하고 attention에 전적으로 의존한다.
    - 병렬 처리가 가능하고 더 작은 학습 시간에서도 번역에서 SOTA 성능을 보였다.
# 2. Background
- 시퀀셜 연산을 줄이는 목적으로 CNN을 사용해 병렬처리를 하려고 했는데, 입출력 간 연관 신호의 거리 의존성을 학습하기 어렵게 만들었다.
- Transformer는 고정된 수의 연산 과정으로 이 부분을 줄였는데, Multi-Head Attention의 효과로 대응된다.
- Self-attention은 intra-attention 으로도 불린다.
    - 시퀀스의 표현을 계산하기 위해 단일 시퀀스의 다른 위치를 연관 시키는 attention 방법이다.
- End-to-end 메모리 네트워크는 Recurrent attention 방법에 기반한다.
- Transformer는 첫 변환 모델로 전적으로 self-attention에 의존한다.
# 3. Model Architecture
- Transformer도 인코더 디코더 모델의 구조를 전적으로 따르고, auto-regressive 하다.
- stacked self-attention과 point-wise, fully-connected layer를 인코더와 디코더에 사용한다.
## 3.1. Encoder and Decoder Stacks
### Encoder
- N(6)개의 동일한 레이어로 구성된다. 각 레이어는 두 서브 레이어를 가진다.
- 서브 레이어는 multi-head self-attention과 position-wise fully connected feed-forward network를 가진다.
- 두 서브 레이어 각각에 residual-connection과 Layer Normalization을 채용했다
- residual-connection 을 쉽게 사용하기 위해 모든 하위 계층과 임베딩은 동일한 512 차원의 출력을 사용한다.
### Decoder
- N(6)개의 동일한 레이어로 구성된다. 인코더의 두 서브 레이어에 세번째 서브 레이어를 추가 했다
    - 인코더 스택의 출력에 대해 multi-head attention을 수행한다.
- 두 서브 레이어 각각에 residual-connection과 Layer Normalization을 채용했다
- 디코더의 self-attention을 수정해서 subsequent 위치의 참여를 예방했다.
    - 마스킹을 사용해서 예방 했다.
### 3.2. Attention
- query와 key-value 쌍의 셋을 output으로 매핑한 것으로 attention 함수를 설명할 수 있다.
    - query, key, value, output 은 모두 벡터들이다.
- output은 values의 가중합으로 각 value에 할당된 가중치는 해당 key를 사용하는 query의 compatibility 함수로 계산된다.
