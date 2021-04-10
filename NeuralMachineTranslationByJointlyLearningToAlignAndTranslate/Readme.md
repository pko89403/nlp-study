### Abstract
- 이전 세대의 번역 모델의 고정 길이 벡터 사용이 병목이다.
- 확장, 입력 문장의 일부를 자동으로 검색하기 위한 모델.
- soft-alignment
### Introduction
- 뉴럴 번역 모델은 하나의 큰 신경망을 구축하고 학습하는 것을 시도했다.
- 인코더 - 디코더 시스템은 합동 학습을 했다. 입력 문장을 바르게 번역할 확률을 최대화 하기 위해서
- 입력 문장의 모든 필요한 정보를 고정된 길이의 벡터로 압축했는데 뉴럴 네트워크를 긴 문장에 대처하기 힘들게 만들어었다.
- 특히 학습 데이터 셋 보다 입력 문장의 길이가 더 길때에 대해서
- 이 문제를 해결하기 위해 인코더 디코더 모델을 확장해서 align과 translate를 함께 학습하게 했다.
- 입력 문장에서 가장 관련성 있는 정보의 일종의 위치를 검색했다. 
- 그 다음 타겟 단어를 예측한다. 검색된 위치와 연관되는 context 벡터와 모든 이전 타겟 단어들에 기반해서
- 전체 입력 문장을 고정된 길이의 벡터로 인코딩하지 않고 벡터의 시퀀스로 인코딩 하고 벡터 들의 부분 집합을 고른다.
- align과 translate를 jointly learning하는 접근 방법
### Background : Nerual Machine Translation
- 번역은 주어진 입력 문장 x에서 타겟 문장 y를 찾는 y에 대한 조건 부 확률을 최대화 하는 것과 동일하다.
- 조건 부 분포가 학습된다. 이 분포를 직접 학습 하기 위해 뉴럴 네트워크를 사용한다.
- 첫째, 인코딩, 두번째, 디코딩
### RNN ENCODER-DECORDER
- 벡터 시퀀스 x를 벡터 c로 인코딩 한다.
- LSTM
- 주어진 context 벡터 c와 모든 이전에 예측된 단어들로 디코더가 다음 단어 y를 예측
- 하이브리드 RNN과 역-Conv 뉴럴 네트워크
### LEARNING TO ALIGN AND TRANSLATE
- bidirectional RNN을 encoder 그리고 번역을 디코딩 하는 동안 입력 문장을 통해 검색을 모방하는 디코더
- 확률은 각 타겟 단어 y에 대해서 별도의 context 벡터의 영향을 받는다.
- context 벡터는 annotation 시퀀스 h 에 의존한다.
- annotation은 입력 시퀀스의 i 번째 단어를 둘러싼 부분에 중점을 둔 전체 입력 시퀀스 에 대한 정보
- 위치 j 주변의 입력과 위치 i 의 출력
- alignment 모델, soft alignment를 직접 연산한다.
- 모든 annotation 들의 가중 합을 기대 annotation로 계산한다.
- 디코더를 attetion 메커니즘을 가지게 한다
### ENCODER: BIDIRECTIONAL RNN FOR ANNOTATING SEQUENCES
- bidirectional RNN. BiRNN은 포워드 백워드 RNN으로 구성된다.

