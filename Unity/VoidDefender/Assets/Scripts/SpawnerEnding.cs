using UnityEngine;
using System.Collections;

public class SpawnerEnding : MonoBehaviour {
	public GameObject[] attackerPrefabArray;
	// Use this for initialization
	void Start () {
		Spawn(attackerPrefabArray[Random.Range(0, attackerPrefabArray.Length)]);
	}
	
	
	void Spawn(GameObject attackerGameObject)
	{

		GameObject myAttacker = Instantiate(attackerGameObject) as GameObject;
		myAttacker.transform.parent = transform;
		myAttacker.transform.position = transform.position;
		
	}
}
