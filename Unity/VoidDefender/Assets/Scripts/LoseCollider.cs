using UnityEngine;
using System.Collections;

public class LoseCollider : MonoBehaviour {
	private LevelManager levelManager;
	// Use this for initialization
	void Start () {
		levelManager = GameObject.FindObjectOfType<LevelManager>();
		if (!levelManager)
		{
			levelManager = new LevelManager();//Need to name this as Projectiles

		}
	}

	void OnTriggerEnter2D(Collider2D col)
	{
		//If an enemy gets past us, we lose
		GameObject obj = col.gameObject;
		if (!obj.GetComponent<Attacker>())
		{
			//abort if not colliding with Attacker
			return;
		}
		else {
			levelManager.LoadLevel("L03b_Lose");

		}
		//Debug.Log(name + " trigger enter");
	}
}
