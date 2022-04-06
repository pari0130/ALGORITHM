package INFLEARN.STEP06

import java.util.*


// https://cote.inflearn.com/contest/10/problem/06-01
// 선택 정렬을 이용하여 정렬 리턴
/*
in
6
13 5 11 7 23 15

out
5 7 11 13 15 23
*/
fun solution(n: Int, arr: IntArray): IntArray {
    for (i in 0 until n - 1) {
        var idx = i
        for (j in i + 1 until n) {
            if (arr[j] < arr[idx]) idx = j
        }
        val tmp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = tmp
    }
    return arr
}

private fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)
    for (i in 0 until n) arr[i] = kb.nextInt()
    for (x in solution(n, arr)) print("$x ")
}