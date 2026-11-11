<script setup lang="ts">
  import type { GitHubResponse, GitHubRepo } from '~/types/github';

  const EMPTY_REPOS: GitHubRepo[] = [];

  const colorMode = useColorMode();

  // Build-time list, embedded in the prerendered payload.
  const { data: prerendered, status } = await useFetch<GitHubResponse>(
    '/api/github',
    {
      key: 'github-repos',
    },
  );

  // Fresh list after hydration. A separate key, so a failed GitHub call
  // (the API returns 502) leaves the prerendered list on screen instead of
  // replacing it with an empty one.
  const { data: live } = useFetch<GitHubResponse>('/api/github', {
    key: 'github-repos-live',
    server: false,
  });

  const data = computed(() => live.value ?? prerendered.value);

  const FEATURED_REPOS = ['tileserver-rs', 'v-maplibre'];

  const pinnedRepos = computed(() => {
    if (!data.value?.pinned) return EMPTY_REPOS;
    const pinned = [...data.value.pinned];
    const featured = pinned.filter((r) => FEATURED_REPOS.includes(r.name));
    const rest = pinned.filter((r) => !FEATURED_REPOS.includes(r.name));
    return [...featured, ...rest];
  });

  const repos = computed(() => data.value?.repos ?? EMPTY_REPOS);

  function langDotStyle(repo: GitHubRepo): { backgroundColor: string } {
    return { backgroundColor: repo.languageColor ?? 'var(--muted)' };
  }

  function formatStars(count: number): string {
    if (count >= 1000) return `${(count / 1000).toFixed(1)}k`;
    return count.toString();
  }

  // YOUR SPECIFIC PROJECTS
  const highlightedProjects = [
    {
      name: '51_Web_Projects',
      description: 'Collection of 51 web projects',
      url: 'https://github.com/jaikaran109/51_Web_Projects',
      stars: 0,
      forks: 0,
      language: 'HTML',
    },
    {
      name: 'SolarSense-An-AI-Powered-Smart-Solar-Planning-and-Feasibility-Platform',
      description: 'AI-powered solar planning platform',
      url: 'https://github.com/jaikaran109/SolarSense-An-AI-Powered-Smart-Solar-Planning-and-Feasibility-Platform',
      stars: 0,
      forks: 0,
      language: 'Python',
    },
    {
      name: 'Project-Drishti',
      description: 'AI for healthcare applications',
      url: 'https://github.com/jaikaran109/Project-Drishti',
      stars: 0,
      forks: 0,
      language: 'Python',
    },
    {
      name: 'DSA',
      description: 'Data Structures & Algorithms implementations',
      url: 'https://github.com/jaikaran109/DSA',
      stars: 0,
      forks: 0,
      language: 'C++',
    },
    {
      name: 'Kaizen',
      description: 'Continuous improvement tools',
      url: 'https://github.com/jaikaran109/Kaizen',
      stars: 0,
      forks: 0,
      language: 'JavaScript',
    },
    {
      name: 'Machine-Learning',
      description: 'Machine Learning projects',
      url: 'https://github.com/jaikaran109/Machine-Learning',
      stars: 0,
      forks: 0,
      language: 'Python',
    },
  ];
</script>
