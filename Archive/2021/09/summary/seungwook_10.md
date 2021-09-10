# Eyes Tell All: Irregular Pupil Shapes Reveal GAN-Generated Faces
## Hui Guo et al., SUNY - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**: 
* Reference 이후를 제외하면 4페이지밖에 되지 않는 짧은 paper며, conference에 제출된 것 같진 않다.
* Arxiv-sanity top hype, Deep Learning monitor super-hot 2개를 동시에 달성해서 읽어보게 되었다.
* 연구적인 면의 contribution을 제안하진 않지만, GAN-generated face를 구분할 수 있는 유의미한 finding을 소개한다. 향후 face generating GAN 연구를 할 경우 꼭 읽어보면 좋을 것 같다는 생각이 들었다.
* Writing 자체는 (문법) 뛰어나진 않지만, 재미로 읽어보기 나쁘지 않았다. 인터넷에서 fake 얼굴인지 구분할 수 있는 좋은 방법인 것 같다.
* 논문에 언급된 바는 아니지만, Pupil의 색이 그다지 밝지 않아 pupil과의 segmentation이 쉽지 않은 경우 (예: 대부분의 한국인), 잘 작동하지 않을 수 있을 것 같다.

**Task**: Discriminating GAN-generated Faces

**Motivation / Contributions**
* GAN-generated faces are difficult to discern from real faces
* can be abused for malicious purposes, causing social disturbance
* Proposes/confirms that GAN-generated faces have visible artifacts & inconsistencies in the eye regions
    * In particular, the boundary of GAN-generated pupils **is not elliptical**
        * pupils are suppoed to be elliptical in shape
    * uses this to propose a simple baseline to effectively discriminate GAN-generated faces

**Method outline**
1. Pupil Segmentation and Boundary Detection
* Face detector -> landmark extractor -> crop only the eye region
* Use *EyeCool* to extract pupil mask & boundary
    * *EyeCool* is an existing model
2. Ellipse fitted Pupil Mask
* Using **Least Square-based ellipse fitting method** on the outer boundary of predicted pupil mask
3. Measure BIoU between Predicted Pupil Mask & Ellipse fitted mask
* Why not use normal Mask IoU? 
    * this measure values or pixels equally, less sensitive to boundaries.
    * but we are interested in the boundary
* Uses Boundary IOU (BIOU) instead!
    * IoU between boundaries of the two shapes
    * The "width" of the boundaries is a hyperparameter, set to 4 here.
        * "width": distance from the boundary contours.
        * When the "width" is large enough, BIoU == IoU
* **larger BIoU: real face**
* **Lower BIoU: fake, generated face**

사실 어느정도 눈으로도 구분이 가능하다고 한다.

**Experiments & Discussion**
* Real faces from **FlickrFaces-HQ (FFHQ) dataset**
* Fake faces from **StyleGAN2**

1. Clear separation in in BIoU score distribution of real/fake faces
    * sufficient to discern fake faces
2. Increasing "width" hyperparameter of BIoU worsens the results
    * boundary information is indeed more information

Limitations:
* may have False positives when pupil shapes are non-elliptical in real faces
    * due to diseases / infections
* Occlusion/Failed pupil segmentation leads to wrong results
