# Troubleshooting Log

## git commit --amend
- 참여자: Sangheon Lee
- 상황: 최근 커밋 메시지가 모호했다.
- 명령: `git commit --amend`
- 결과: 최근 커밋 메시지를 명확하게 고쳤다.
- 배운 점: 공유된 커밋에는 팀 합의 없이 amend를 쓰지 않는다.

## git reset --soft HEAD~1
- 참여자: KANGSIK-SEO
- 상황: push 전 `update`라는 모호한 커밋을 만들었다.
- 명령: `git reset --soft HEAD~1`
- 결과: 커밋만 취소되고 변경사항은 staged 상태로 남았다.
- 배운 점: reset soft는 변경사항을 지우지 않고 커밋만 되돌릴 때 쓴다.

## git revert
- 참여자: giyeop-cody
- 상황: 이미 원격에 push된 잘못된 커밋을 취소해야 했다.
- 명령: `git revert <commit_sha>`
- 결과: 기존 커밋을 삭제하지 않고 되돌리는 새 커밋을 만들었다.
- 배운 점: 공유된 커밋은 reset보다 revert가 안전하다.

## git stash / git stash pop
- 참여자: giyeop-cody
- 상황: 작업 중 main 최신 변경을 먼저 확인해야 했다.
- 명령: `git stash push -m "wip: stash note"`, `git stash pop`
- 결과: 작업 중 변경을 임시 보관했다가 다시 복원했다.
- 배운 점: 브랜치 이동 전 작업 중인 변경사항을 안전하게 보관할 수 있다.
