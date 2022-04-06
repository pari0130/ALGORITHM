package INFLEARN.STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-10
// 현재 위치가 상하좌우 값 보다 큰 위치(봉우리) 가 몇개 있는지 확인
/*
in
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

out
10
*/
private fun solution(n: Int, arr: Array<IntArray>): Int {
    var answer = 0
    val dx = listOf(-1, 0, 1, 0)
    val dy = listOf(0, 1, 0, -1)

    for (i in 0 until n) {
        for (j in 0 until n) {
            var flag = true
            // 4방향 탐색 부분
            for (k in 0 until 4) {
                val nx = i + dx[k]
                val ny = j + dy[k]
                // nx >= 0 && nx < n => nx in 0 until n
                if (nx in 0 until n && ny >= 0 && ny < n && arr[nx][ny] >= arr[i][j]) {
                    flag = false
                    break
                }
            }
            if (flag) answer++
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = Array(n) { IntArray(n) }
    for (i in 0 until n) {
        for (j in 0 until n) {
            arr[i][j] = kb.nextInt()
        }
    }
    print(solution(n, arr))
}