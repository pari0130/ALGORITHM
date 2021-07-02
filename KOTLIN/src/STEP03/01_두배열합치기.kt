package STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-01
// 오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
/*
in
3
1 3 5
5
2 3 6 7 9

out
1 2 3 3 5 6 7 9
*/
private fun solution(n: Int, m: Int, a: IntArray, b: IntArray): ArrayList<Int> {
    val answer = ArrayList<Int>()
    var p1 = 0
    var p2 = 0

    // 배열의 크기만큼 진행하면서 두 수 중 작은 수를 먼저 answer 에 저장 하는 방식
    while (p1 < n && p2 < m) {
        if (a[p1] < b[p2]) {
            answer.add(a[p1++])
        } else {
            answer.add(b[p2++])
        }
    }
    while (p1 < n) answer.add(a[p1++])
    while (p2 < m) answer.add(b[p2++])

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val a = IntArray(n)
    for (i in 0 until n) {
        a[i] = kb.nextInt()
    }
    val m = kb.nextInt()
    val b = IntArray(m)
    for (i in 0 until m) {
        b[i] = kb.nextInt()
    }
    solution(n, m, a, b).forEach {
        print("$it ")
    }
}