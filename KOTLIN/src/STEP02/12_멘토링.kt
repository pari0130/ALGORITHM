package STEP02

import java.util.*

// https://cote.inflearn.com/contest/10/problem/02-12
// a학생이 b학생의 멘토가 되려면 수학성적이 앞서야 한다. 수학성적이 앞서서 멘토가 되는 경우를 구해야 함.
/*
in
4 3
3 4 1 2
4 3 2 1
3 1 4 2

out
3
*/
private fun solution(n: Int, m: Int, arr: Array<IntArray>): Int {
    var answer = 0
    for (i in 1..n) {
        for (j in 1..n) {
            var cnt = 0
            for (k in 0 until m) {
                var pi = 0
                var pj = 0
                for (s in 0 until n) {
                    if (arr[k][s] == i) pi = s
                    if (arr[k][s] == j) pj = s
                }
                if (pi < pj) cnt++
            }
            if (cnt == m) {
                answer++
            }
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val m = kb.nextInt()
    val arr = Array(m) { IntArray(n) }
    for (i in 0 until m) {
        for (j in 0 until n) {
            arr[i][j] = kb.nextInt()
        }
    }
    println(solution(n, m, arr))
}