package INFLEARN.STEP03

import java.util.*


// https://cote.inflearn.com/contest/10/problem/03-02
// A, B 두 개의 집합이 주어지면 두 집합의 공통 원소를 추출하여 오름차순으로 출력하는 프로그램을 작성하세요.
/*
in
5
1 3 9 5 2
5
3 2 5 7 8

out
2 3 5
*/
private fun solution(n: Int, m: Int, a: IntArray, b: IntArray): ArrayList<Int> {
    val answer = ArrayList<Int>()
    Arrays.sort(a) // #팁 정렬
    Arrays.sort(b)
    var p1 = 0
    var p2 = 0
    while (p1 < n && p2 < m) {
        if (a[p1] == b[p2]) {
            answer.add(a[p1++])
            p2++
        } else if (a[p1] < b[p2]) p1++ else p2++
    }
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
    for (x in solution(n, m, a, b)) print("$x ")
}