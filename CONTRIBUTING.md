# 기여 가이드라인
원문: https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md<br>
번역자: [tucan9389](https://github.com/tucan9389)

## Pull Request 체크리스트

PR을 날리기 전에 아래 리스트를 확인해보세요.
- [기여 가이드라인(contributing guidelines)](https://github.com/tensorflow/tensorflow/edit/master/CONTRIBUTING.md) 읽어보기.
- [행동강령(Code of Conduct)](https://github.com/tensorflow/tensorflow/edit/master/CODE_OF_CONDUCT.md) 읽어보기.
- [Contributor License Agreement (CLA)](https://cla.developers.google.com/)에 서명을 했는지 확인하기.
- 나의 변경사항이 이 [가이드라인](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md#general-guidelines-and-philosophy-for-contribution)과 일관성이 있는지 확인하기.
- 변경사항이 [코딩 스타일](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md#c-coding-style)에 적합한지.
- [유닛 테스트](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md#running-unit-tests) 돌려보기.

## 어떻게 컨트리뷰터가 되고 여러분의 코드를 제출할까요

### 컨트리뷰터 라이센스 계약

우리는 여러분의 조각을 받아드리고 싶습니다! 받아드리기 전에, 몇가지 법적 부분을 인지해야합니다.

개인 또는 법인 컨트리뷰터 라이센스 계약(CLA)를 작성해주세요.

* 만약 당신이 개인적으로 기존의 소스코드를 짜고 있고 당신의 지적 재산권을 가지고 있다고 확인할 경우, [개인 CLA](https://code.google.com/legal/individual-cla-v1.0.html)에 서명해야합니다.
* 만약 당신이 회사에서 기여하기를 원하는 경우, [법인 CLA](https://code.google.com/legal/corporate-cla-v1.0.html)에 서명해야합니다.

위의 두 링크 중 적절한 CLA에 들어가서 서명을 하고 되돌아오는 지시사항을 따르십시오. 우리가 서명을 받으면 당신의 PR을 수용할 수 있게 됩니다.

***주의:*** *CLA에 서명한 사람만 기존 코드를 주 저장소에 받아드릴 수 있습니다.*

### 코드 기여하기

Tensorflow를 개선하고 싶으면 우리에게 PR을 날려주십시오! 처음인 사람을 위해 Github에 [howto](https://help.github.com/articles/using-pull-requests/) 페이지가 있습니다.

여러분의 PR을 리뷰하기위해 Tensorflow 팀 맴버들이 지정될 것 입니다. PR이 승인되고 CI를 통과하면 우리가 PR을 머지(merge)시킬것입니다.
어떤 PR에대해서는 그 패치를 먼저 우리의 내부적인 버전 관리 시스템에 적용시킬 것입니다. 그리고 나중에 기존의 PR이 클로즈되는 시점에서 그 변경사항을 새로운 커밋으로 내보냅니다. 그 PR에 있는 커밋들은 작성자로써 PR 창작자와함께 한 커밋으로 만들어질 것 입니다. 이 PR은 내부적으로 보류중인 병합으로 표시될 것 입니다.

기여를 하고 싶지만, 어디서부터 시작해야할지 모르겠다면 ["contributions welcome" 라벨이 붙어있는 이슈들](https://github.com/tensorflow/tensorflow/labels/stat%3Acontributions%20welcome)을 한번 보십시오.
이 이슈들은 특별히 외부 컨트리뷰터들에게 적합하다고 생각하는 것이며, 우리가 지금 바로 처리할 것은 아닐 것 입니다. 한 이슈에서 시작하기로 결정했으면 코멘트를 달아서 당신이 작업한다는 것을 다른 사람들이 알 수 있도록 해주십시오. 도움이 필요하면 이슈 코멘트 스레드를 사용하여 요청하십시오.

### 기여 가이드라인과 표준

[리뷰](https://github.com/tensorflow/tensorflow/pulls)를 위해 PR를 날리기 전에, 변경사항들이 가이드라인을 지키는지 아래 Tensorflow 코딩 스타일을 따르는지 확인해 주십시오.

#### 기여에대한 보편적인 가이드라인과 철학

- 새로운 기능을 기여할때는 a) 올바르게 코드를 제안했는지, b) 유지보수 비용을 줄이기위해 미래에 코드가 망가지는 것을 방지하는 것에 도움이 되도록 유닛 테스트를 포함시키세요.
- 버그가 있다는 것은 보통 테스크 커버리지가 불충분하다는것을 의미하기 때문에, 버그 수정은 일반적으로 유닛 테스트를 필요로 합니다. 
- ([tensorflow/core](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core) 혹은 [tensorflow/python](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python) 같은) Tensorflow의 코어한 부분의 코드를 건드릴 때는 API 호환성을 염두하세요. Tensorflow는 버전 1까지 왔습니다. 그러므로 메이저 릴리즈 없이는 이전 버전과 호환되지 않는 API 변경을 만들어서는 안 됩니다. 당신 PR의 리뷰어는 어떤 API 호환성 이슈에대해 댓글을 달 것 입니다.
- Tensorflow에 새로운 기능을 기여할때는 유지보수 부담이 기본적으로 Tensorflow 팀에게 가게됩니다. 이것은 기여 부분의 이점과 그 기능의 유지보수 비용에대해 비교해야 합니다.
- 완전히 새로운 기능(예를들면 커팅-엣지 알고리즘을 구현한 새로운 op)은 핵심 코드에 이전할지 고려되기 전까지는 [tensorflow/contrib](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib)에서 대기시간을 가질 것입니다.

#### 라이센스

새로운 파일의 상단에 라이센스를 넣어주십시오.

- [C/C++ license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/op.cc#L1)
- [Python license example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/nn.py#L1)
- 
Bazel BUILD 파일은 라이센스 섹션을 포함시켜야합니다. 예를들면 [BUILD example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/BUILD#L61).
