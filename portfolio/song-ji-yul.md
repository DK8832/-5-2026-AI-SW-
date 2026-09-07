# 송지율 · 개인 개발 포트폴리오

인천전자마이스터고등학교 인공지능전자과 2학년 · innovation 대표팀원

영상 인식 프로그램에서 모델과 화면을 연결하는 경험을 시작으로, 학습에 필요한 웹 도구와 Linux 실행 기록, 공공데이터 서비스 기획으로 활동을 넓혔습니다. 이번 AgentBridge의 신청 분야는 UI/UX입니다.

## 1. AI 분리배출 도우미 · 모델 연동과 결과 표시

**활동:** 2026 SW미래채움 AI·SW 고교 챌린지 피지컬 AI 팀 프로젝트. 당시 팀명은 GOAT이며 노문선·송지율·황재찬이 함께했습니다.

**문제와 선택:** 카메라에 비친 물체의 분리배출 종류를 안내하는 프로그램을 구상했습니다. 자동 분류함까지 계획했으나 하드웨어 수급 문제로, 사전학습 YOLOv8 모델과 분류 매핑을 결합한 소프트웨어 결과물로 범위를 조정했습니다.

**본인 역할:** 발표자료 3·4·9쪽에 모델 연동과 구현 담당으로 기록되어 있습니다. `YOLO('yolov8n.pt')` 모델 로드, 웹캠 입력 연동, `results.boxes` 반복문, 좌표·클래스·신뢰도 추출 및 박스·문자 표시가 담당 내용입니다.

```python
results = model(frame, imgsz=IMGSZ, verbose=False)[0]
for box in results.boxes:
    cls_name = model.names[int(box.cls[0])]
    if cls_name in EXCLUDE:
        continue
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = float(box.conf[0]) * 100
    trash_type = TRASH_MAP.get(cls_name, cls_name)
```

감지 결과를 객체별로 순회하면 한 프레임의 여러 물체를 처리할 수 있습니다. 신뢰도는 모델 출력값에 100을 곱해 표시하고, 매핑표에 없는 클래스는 원래 이름을 유지합니다. 따라서 코드의 표시 신뢰도를 전체 분류 정확도로 해석하지 않습니다.

**결과와 학습:** 원본 `project.py`에서 웹캠 입력부터 추론·매핑·시각화·종료까지의 구조를 확인할 수 있습니다. 발표자료에는 병·책·컵 인식과 사람 제외 동작을 확인한 내용이 기록되어 있습니다. 학습 데이터셋을 새로 구축한 성과나 정량 정확도·FPS, STM32·서보모터 연동 성과는 포함하지 않습니다.

증빙: [원본 코드](../evidence/ai-recycling/project.py), [발표자료 역할·코드 원문 발췌](../evidence/ai-recycling/source-excerpts.md), [프로젝트 설명](../projects/ai-recycling-assistant.md)

## 2. CODE:90 · 학습 문제를 웹 도구로 구성

**필요:** SQL·Python·Java·Linux 학습 내용을 반복 확인하고, 오답을 다시 풀 수 있는 도구가 필요했습니다.

**활동 범위:** 기존 학습자료와 요구사항을 제공하고, Codex를 활용해 코드·문제·테스트 초안을 구성한 학습도구 제작 기록입니다. 전부 직접 작성한 코드로 제시하지 않습니다.

공개 결과물은 SQL 20문제와 나머지 세 영역 각 10문제, 총 50문제입니다. 문제별 즉시 채점과 90분 모의 모드를 구분하고, `localStorage`에 답안·현재 위치·남은 시간을 저장합니다. 문제 데이터는 `questions.js`, 채점·집계 함수는 `core.mjs`, 화면 동작은 `app.js`로 나뉩니다.

**설계에서 다룬 점:** 즉시 해설을 보는 연습과 해설을 숨기는 모의시험의 목적 차이, 새로고침 후 학습 상태 복원, 오답 ID를 이용한 재학습 구성을 다뤘습니다. 문제 수와 정답 인덱스, 0점·100점, CSV 이스케이프 등을 검사하는 테스트가 공개되어 있습니다.

증빙: [공개 저장소](https://github.com/DK8832/programming-cert-practical-study-tool), [개선 과정](https://github.com/DK8832/programming-cert-practical-study-tool/blob/main/docs/IMR_PORTFOLIO.md), [핵심 채점 로직](https://github.com/DK8832/programming-cert-practical-study-tool/blob/main/core.mjs), [자동 테스트](https://github.com/DK8832/programming-cert-practical-study-tool/blob/main/test/core.test.mjs)

## 3. Linux 터미널 실습 · 실행 결과를 다시 확인하는 학습

파일·권한·텍스트·압축·프로세스·시스템 정보의 여섯 영역을 Bash 실습과 Python 검증기로 정리했습니다. 이 활동도 Codex를 활용한 스크립트·문서 제작 및 실행 검증 기록입니다.

**문제 해결 기록:** Windows의 CRLF 줄바꿈이 Bash에 들어가 명령 오류가 발생한 기록이 있습니다. LF로 수정하고 `pipefail`을 추가해 `tee` 뒤로 오류가 숨지 않도록 했습니다. 수정 후 GitHub Actions 실행 `33694870725`가 성공했으며, 원본 기록에는 `CHECKS_PASSED=8`, `LAB_STATUS=PASS` 확인 내용이 남아 있습니다.

명령이 성공해 보이는 것과 실제 파일·권한·로그를 다른 명령으로 다시 검사하는 것의 차이를 다룬 학습입니다. 자격 취득이나 시험 점수 향상을 뜻하지 않습니다.

증빙: [실습 코드와 과정](https://github.com/DK8832/linux-master-level2-terminal-lab), [성공한 실행 기록](https://github.com/DK8832/linux-master-level2-terminal-lab/actions/runs/33694870725), [문제 해결 기록](https://github.com/DK8832/linux-master-level2-terminal-lab/blob/main/docs/IMR_PORTFOLIO.md)

## 4. 청주 안심동선 · AI·데이터 서비스 기획

네 명이 함께한 기존 설계 제안입니다. 제안서 17쪽에 팀 대표·AI 및 데이터 분석 담당으로 공공데이터 수집, 위험도 모델 설계, 결과 검증 역할이 기록되어 있습니다.

팀 제안서는 사고·인구·시설·도로 데이터를 100m 격자로 결합하고 위험지점과 개선 원인을 함께 보여 주는 구조를 담고 있습니다. 가중치 기반 점수와 RandomForest/XGBoost 비교, 과거 사고지역과의 검증을 후속 구현 계획으로 제시했습니다. 이 포트폴리오에는 **문제 정의와 설계 참여 경험**으로 기재합니다.

증빙: [제안서 원본 발췌](../evidence/cheongju/source-pages.pdf), [공동 프로젝트](../projects/cheongju-safe-route.md)

## 5. 기술 탐색과 현재 프로젝트

- **Dell Technologies Forum 2026:** 2026년 8월 25일 행사 방문을 계기로 AI 인프라를 데이터·연산·플랫폼·운영/보안·성과의 다섯 층으로 재구성한 학습 기록이 있습니다. 방문 증빙과 행사 후 학습 정리를 구분했습니다. [학습 자료](https://github.com/DK8832/dell-forum-2026-ai-infrastructure)
- **AgentBridge:** 2026년 9월 3일 제출 문서상 대표팀원이며 UI/UX 분야입니다. 초보자용 도구 추천과 설치 안내를 다루는 이번 팀 프로젝트입니다. 세부 기능별 개인 기여는 신청 분야와 구분하여 [출품작 자료](../projects/agentbridge.md)에 설명했습니다.

## 역량 요약

| 역량 | 확인 자료 |
|---|---|
| Python·OpenCV·YOLO 결과 처리 | 모델 로드, 다중 객체 반복, 좌표·신뢰도 표시 코드와 역할표 |
| 학습용 웹 서비스 구조화 | CODE:90의 문제·채점·화면 분리와 이어 풀기 설계 |
| 실행 오류 분석 | Bash 줄바꿈 오류, 파이프 실패 전파, 실제 실행 로그 |
| 데이터 서비스 기획 | 청주 안심동선 데이터 결합·검증 구조 및 제안서 역할 |
| 기술 학습의 확장 | AI 인프라 행사 후 학습 구조와 후속 실습 질문 |

[전체 목차](README.md) · [자료의 출처와 범위](../evidence/README.md)
