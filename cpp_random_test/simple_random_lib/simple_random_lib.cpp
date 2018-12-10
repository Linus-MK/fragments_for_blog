// simple_random_lib.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//

#include "pch.h"
#include <iostream>

// https://cpprefjp.github.io/reference/random.html のリンク先の各ライブラリからコピー、改変

#include <random>

int main()
{
	std::random_device seed_gen;
	std::default_random_engine engine(seed_gen());

	// 0以上9以下の値を等確率で発生させる
	std::uniform_int_distribution<> dist1(0, 9);

	for (std::size_t n = 0; n < 50; ++n) {
		// 一様整数分布で乱数を生成する
		int result = dist1(engine);

		std::cout << result << ",";
	}
	std::cout << "\n\n";

	// 平均0.0、標準偏差1.0で分布させる
	std::normal_distribution<> dist2(0.0, 1.0);

	for (std::size_t n = 0; n < 50; ++n) {
		// 正規分布で乱数を生成する
		double result = dist2(engine);

		std::cout << result << ",";
	}
	std::cout << "\n\n";

	// 確率0.7でtrueを生成し、確率0.3(1.0 - 0.7)でfalseを生成する
	std::bernoulli_distribution dist3(0.7);

	for (std::size_t n = 0; n < 50; ++n) {
		// 乱数を生成する
		bool result = dist3(engine);

		std::cout << result << ",";
	}
	std::cout << "\n\n";

}

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
