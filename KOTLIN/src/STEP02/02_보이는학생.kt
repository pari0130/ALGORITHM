package STEP02

import java.lang.StringBuilder
import java.util.Scanner

// https://cote.inflearn.com/contest/10/problem/02-02
// 8
// 130 135 148 140 145 150 150 153 >> 5
private fun solution(n : Int, arr: IntArray): Int {
    var answer = 1
    var max = arr[0] // 첫뻔째 학생은 초기값으로 제일 큼

    for(i in 1 until n) {
        if(arr[i] > max){
            answer ++
            max = arr[i]
        }
    }

    return answer
}

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)

    for(i in 0 until n){
        arr[i] = kb.nextInt()
    }

    println(solution(n, arr))
}