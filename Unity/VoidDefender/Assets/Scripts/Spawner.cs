using UnityEngine;
using System.Collections;

public class Spawner : MonoBehaviour {
	private GameObject parent;
	public GameObject[] attackerPrefabArray;
	// Use this for initialization
	void Start () {

		parent = GameObject.Find("Enemies");
		if (!parent)
		{
			parent = new GameObject("Enemies");//Need to name this as Projectiles

		}
	}
	
	// Update is called once per frame
	void Update () {
		if (Time.timeSinceLevelLoad > 10)
		{
			foreach (GameObject thisAttacker in attackerPrefabArray)
			{
				if (IsTimeToSpawn(thisAttacker))
				{
					Spawn(thisAttacker);
				}
			}
		}
		
	}


	bool IsTimeToSpawn(GameObject attackerGameObject)
	{
		Attacker attacker = attackerGameObject.GetComponent<Attacker>();
		float meanSpawnDelay = attacker.seenEverySeconds;
		float spawnsPerSecond = 1 / meanSpawnDelay;
		if (Time.deltaTime > meanSpawnDelay)
		{
			Debug.LogWarning("Spawn rate capped by frame rate");
		}
		float threshold = spawnsPerSecond * Time.deltaTime / 5;//divide by 5 lanes
		return (Random.value < threshold);//random chance of spawning character, averaging once per whatever
		
		
	}
	void Spawn(GameObject attackerGameObject)
	{

		GameObject myAttacker = Instantiate(attackerGameObject) as GameObject;
		myAttacker.transform.parent = transform;
		myAttacker.transform.position = transform.position;
		
		//newProjectile.transform.position = gun.transform.position;
	//	spawnNumber--;
		//print(spawnNumber);
	}
	/*void Spawn()
	{
		int random = Random.Range(0, 2);
		GameObject newEnemy = Instantiate(attackerPrefabArray[random], gameObject.transform.position, Quaternion.identity) as GameObject;

		newEnemy.transform.parent = parent.transform;
		//newProjectile.transform.position = gun.transform.position;
		spawnNumber--;
		print(spawnNumber);
	}*/
}
