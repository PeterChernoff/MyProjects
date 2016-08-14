using UnityEngine;
using System.Collections;

public class Shooter : MonoBehaviour {

	public GameObject projectile, gun;
	private GameObject parent;
	private Animator animator;
	private Spawner myLaneSpawner;
	void Start()
	{
		//animator = GetComponent<Animator>();
		animator = GameObject.FindObjectOfType<Animator>();
		parent = GameObject.Find("Projectiles");
		if (!parent)
		{
			parent = new GameObject("Projectiles");//Need to name this as Projectiles

		}
		SetMyLaneSpawner();
		//print(myLaneSpawner);
	}

	void SetMyLaneSpawner()
	{
		Spawner[] spawnerArray = GameObject.FindObjectsOfType<Spawner>();
		foreach (Spawner spawner in spawnerArray)
		{
			if (spawner.transform.position.y == transform.position.y)
			{
				myLaneSpawner = spawner;
				return;
			}
		}
		Debug.LogError(name + " can't find spawner in lane");
	}
	void Update()
	{
		if (IsAttackerAheadInLane() && gameObject)
		{
			animator.SetBool("isAttacking", true);

		}
		else
		{
			animator.SetBool("isAttacking", false);
		}
	}
	private bool IsAttackerAheadInLane()
	{
		//Exit if no attackers in lane
		if (myLaneSpawner.transform.childCount <= 0)
		{
			return false;
		}

		//If there are attackers, are they ahead
		foreach (Transform attacker in myLaneSpawner.transform)//the gameObject.transform allows us to find children
		{
			if (attacker.position.x > transform.position.x)
				return true;
		}
		//attackers in lane but behind
		return false;

	}
	private void FireGun()
	{
		
		//animator can reach into fire method
		GameObject newProjectile = Instantiate(projectile, transform.Find("Gun").position, Quaternion.identity) as GameObject;
		if (newProjectile)//only do this if there's a projectile
		{
			newProjectile.transform.parent = parent.transform;
			//newProjectile.transform.position = gun.transform.position;
		}


	}

	
}
