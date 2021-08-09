# MDETR - Modulated Detection for End-to-End Multi-Modal Understanding
## Aishwarya Kamath, Yann LeCun et al., NYU | Facebok - ICCV 2021 Oral
#### Summarized by Seungwook Kim
---
**Task**: Multi-model reasoning using modulated detector
* Largely inspired by DETR

**Main Idea**: 
1. Multi-modal models rely on off-the-shelf object detection
    * which is usually frozen, does not facilitate end-to-end training (lacks reasoning!)
    * same start as DETR
2. MDETR relies on **text** and **aligned boxes** for supervision
    * "aligned": which part of text corresponds to which part of image
3. SoTA on phrase grounding and referring expression comprehension for both real & synthetic datasets
4. Competitive performance on downstream tasks (some SoTA) including:
    * VQA
    * Referring expression segmentation
    * Few-shot long-tailed object detection

**Method**: \
Overall similar to DETR, except:
1. More input tokens
* Language tokens from pretrained RoBERTa model
* Concatenated with CNN visual features (like in DETR) to transformer encoder module.
2. (Potentially) additional Question-Answering specific tokens **concatenated to** object queries at decoder
* For QA-specific purposes, such as "Question type prediction", "Answers to type X questions..."
3. (Train-time) Soft token prediction
* Do not predict **class** for each bbox. Instead, predict the span of tokens from the original text.
* Many words can correspond to one object (bbox)
* Many bboxes can correspond to the same text (a couple of boxes: all boxes are related to "a couple")
* The model is trained to predict a **uniform distribution** over all token positions that correspond to the object
4. Contrastive alignment
* enforces alignment between
    * the embedded representations of the object at the output of the decoder
    * the text representation at the output of the cross encoder

**Results**: \
SoTA & Competitive Results on various V&L tasks (including downstream tasks)

**총평**:
* DETR 구조에서 크게 바뀌지 않았으며, Language를 처리하는 RoBERTa와 따로 이은 것과, image-text alignment supervision을 잘 사용하기 위한 Soft token prediction loss + Contrastive alignment loss 를 자연스럽게 제안한다.
* V&L 분야에서 요즘에 꽤나 많이 본 류의 논문인데 (visual feature + language feature, pass to single transformer), DETR과 아주 비슷한 것도 그렇고, oral로 뽑힐 정도였는지 살짝 의아하긴 하지만 서브미션 당시에는 (올해 초) 상당히 novel한 접근이었을 수도 있겠다는 생각이 든다. 그만큼 transformer가 vision에 응용되는 속도가 빠른 것으로 보인다.
* 1학기에 들었던 V&L 과목에서 TransVG라는, transformer를 사용하여 visual grounding을 하는 arxiv논문을 읽었는데 그 구조와 상당히 비슷하다. 다만 그 논문은 grounding이라 단 하나의 bbox만 예측했으며, ViT의 CLS token처럼 Bbox prediction을 위한 token바로 input 으로 넣었다. Multi-modal work에서 transformer를 보다 다르고 참신하게 사용하는 방법은 없을지 궁금하다.
